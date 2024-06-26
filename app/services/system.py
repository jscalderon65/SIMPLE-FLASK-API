import platform
from flask import Blueprint, jsonify

system_service_blueprint = Blueprint("system_blueprint", __name__)


@system_service_blueprint.route("/system", methods=["GET"])
def get_system_info():
    os_name = platform.system()
    os_version = platform.version()
    os_architecture = platform.machine()
    hostname = platform.node()
    system_info = platform.uname()

    system_info_dict = {
        "os_name": os_name,
        "os_version": os_version,
        "os_architecture": os_architecture,
        "hostname": hostname,
        "system_info": system_info._asdict(),
    }

    return jsonify(system_info_dict)
