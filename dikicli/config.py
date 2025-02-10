import configparser
import logging
import shutil

from dikicli.templates import CONFIG_TEMPLATE

Log = logging.getLogger(__name__)


class Config:
    def __init__(self, config_file, data_dir):
        Log.debug("Config file: %s", config_file.as_posix())
        Log.debug("Data dir: %s", data_dir.as_posix())
        self.config_file = config_file
        self.default_config = {
            "data dir": data_dir.as_posix(),
            "linewidth": "78",
            "colors": "yes",
            "web browser": "default",
        }
        self.config = configparser.ConfigParser(
            defaults=self.default_config, default_section="dikicli"
        )

    @property
    def linewidth(self):
        return int(self.config["dikicli"]["linewidth"])

    @linewidth.setter
    def linewidth(self, value):
        if isinstance(value, int) and value >= 0:
            self.config["dikicli"]["linewidth"] = str(value)
            return
        raise ValueError("Line width must be positive integer, got: %s" % value)

    def read_config(self):
        """
        Read config from a file.

        Invalid config values will be discarded and defaults used
        in their place.
        """
        _config = self.config["dikicli"]
        if self.config_file.is_file():
            Log.debug("Reading config file: %s", self.config_file.as_posix())
            with open(self.config_file, mode="r") as f:
                self.config.read_file(f)

            width = _config.get("linewidth")
            try:
                if int(width) < 0:
                    msg = "Line width must be positive integer, got: %s" % width
                    raise ValueError(msg)
                Log.debug("line width: %s", width)
                _config["linewidth"] = width
            except ValueError as e:
                Log.warning(e)
                Log.warning(
                    "Invalid line width. Using default: %s",
                    self.default_config["linewidth"],
                )
                _config["linewidth"] = self.default_config["linewidth"]
        else:
            Log.debug("No config file")

    def create_default_config(self):
        """Write default config file to disk.

        Backs up existing configuration file.

        Returns
        -------
        filename : string
            Path to config file.
        """
        filename = self.config_file.as_posix()
        Log.info("Creating default config file: %s", filename)
        config_dir = self.config_file.parent
        if not config_dir.exists():
            config_dir.mkdir(parents=True)
        if self.config_file.is_file():
            backup = filename + ".old"
            Log.info("Saving config file backup at: %s", backup)
            shutil.copy(filename, backup)
        with open(self.config_file, mode="w") as f:
            config_string = CONFIG_TEMPLATE.format(
                data_dir=self.default_config["data dir"],
                linewidth=self.default_config["linewidth"],
            )
            f.write(config_string)
        return filename
