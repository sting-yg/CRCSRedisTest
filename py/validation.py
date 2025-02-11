import logging
import json
from pydantic import ValidationError
from TaskDev import ExpectedTaskStructure
import command

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

channel_model_map = {
    'frontMoveStop': ExpectedTaskStructure,
    'backMoveStop': ExpectedTaskStructure,
    'frontMoveArcStop': ExpectedTaskStructure,
    'backMoveArcStop': ExpectedTaskStructure,
    'cmd.move': command.ExpectedMoveActivity,
    'cmd.docking': command.ExpectedDockingActivity,
    'cmd.kiva-turn': command.ExpectedKivaTurnActivity,
    'cmd.cancel-activity': command.ExpectedCancelActivity,
    'cmd.pause': command.ExpectedPause,
    'cmd.resume': command.ExpectedResume,
    'cmd.control-speed': command.ExpectedSpeedControl,
    'cmd.drive-jog': command.ExpectedDriveJog,
    'cmd.clear-alarm': command.ExpectedAlarmClear,
    'cmd.set-map': command.ExpectedSetMap,
    'cmd.init-pose': command.ExpectedInitPose,
    'cmd.conveyor': command.ExpectedConveyorActivity,
    'cmd.lift': command.ExpectedLiftActivity,
    'cmd.start-charge': command.ExpectedChargeStartActivity,
    'cmd.stop-charge': command.ExpectedChargeStopActivity,
    'cmd.tableturn': command.ExpectedTableTurnActivity,
    'cmd.control-ptz': command.ExpectedControlPtzActivity,
    'cmd.get-picture': command.ExpectedGetPictureActivity,
    'cmd.upload-request': command.ExpectedUploadRequestActivity,
    'cmd.set-sound': command.ExpectedSetSound,
    'cmd.set-led': command.ExpectedUSetLed,
}

def validate_data(channel: str, data: str) -> bool:

    if channel not in channel_model_map:
        logging.warning(f"Unknown channel: [{channel}], skipping validation.")
        return False

    try:
        parsed_data = json.loads(data) 
        model = channel_model_map[channel]  
        model(**parsed_data)  
        print('='*100)
        logging.info(f"Channel: [{channel}] ---- data validation Success.")
        print('='*100)
        return True
    except (ValidationError, json.JSONDecodeError) as e:
        logging.warning(f"Channel: [{channel}] ---- data validation Failure. Error: {e}")
        return False
