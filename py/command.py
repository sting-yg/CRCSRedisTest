from typing import List, Optional
from pydantic import BaseModel

# ======================== CROA<->Navigation ====================================
# move path
class ExpectedMovePath(BaseModel):
    index: int
    node: str
    x: float
    y: float
    angle: float
    actionType: int
    isArc: bool
    arcRadius: float
    arcControlPointX: float
    arcControlPointY: float
    speed: float
    obstacleDetectionDistance: List[float]
    obstacleDetectionAreaAtTarget: List[float]
    class Config:
        extra = 'forbid'



# vmarker
class ExpectedVmarker(BaseModel):
    x: float
    y: float
    class Config:
        extra = 'forbid'


# docking method value
class ExpectedDockingMethodValue(BaseModel):
    # slam: Optional[str] = None
    vmarker: List[ExpectedVmarker]
    # qr: Optional[str] = None
    # qrStrip: Optional[str] = None
    # arucoMarker: Optional[bool] = None
    class Config:
        extra = 'forbid'


# docking path
class ExpectedDockingPath(BaseModel):
    index: int
    node: str
    x: float
    y: float
    angle: float
    actionType: int
    speed: float
    obstacleDetectionDistance: List[float]
    obstacleDetectionAreaAtTarget: List[float]
    dockingMethodType: int
    dockingMethodValue: ExpectedDockingMethodValue
    class Config:
        extra = 'forbid'


# MoveActivity
class ExpectedMoveActivity(BaseModel):
    topicId: str 
    activityId: str 
    driveType: int
    doAlign: Optional[bool] = None
    alignAngle: Optional[float] = None
    pathList: List[ExpectedMovePath]
    class Config:
        extra = 'forbid'
    


# DockingActivity
class ExpectedDockingActivity(BaseModel):
    topicId: str 
    inOutType: int 
    activityId: str 
    pathList: List[ExpectedDockingPath]
    class Config:
        extra = 'forbid'


# KivaTurnActivity
class ExpectedKivaTurnActivity(BaseModel):
    topicId: str 
    activityId: str 
    targetAngle: int
    speed: int
    class Config:
        extra = 'forbid'


# CancelActivity
class ExpectedCancelActivity(BaseModel):
    topicId: str
    stopAtNode: Optional[bool] = None
    class Config:
        extra = 'forbid'

# Pause
class ExpectedPause(BaseModel):
    topicId: str
    class Config:
        extra = 'forbid'

# Resume
class ExpectedResume(BaseModel):
    topicId: str
    class Config:
        extra = 'forbid'
    

# SpeedControl
class ExpectedSpeedControl(BaseModel):
    topicId: str 
    speed: float
    class Config:
        extra = 'forbid'


# DriveJog
class ExpectedDriveJog(BaseModel):
    topicId: str
    linearXVelocity: float
    linearYVelocity: Optional[float] = None
    angularVelocity: float
    class Config:
        extra = 'forbid'


# AlarmClear
class ExpectedAlarmClear(BaseModel):
    topicId: str
    class Config:
        extra = 'forbid'


# SetMap
class ExpectedSetMap(BaseModel):
    topicId: str
    filePath: str
    class Config:
        extra = 'forbid'


# InitPose
class ExpectedInitPose(BaseModel):
    topicId: str
    x: float
    y: float
    angle: float
    class Config:
        extra = 'forbid'



# ======================== CROA<->Navigation ====================================



# ConveyorActivity
class ExpectedConveyorActivity(BaseModel):
    topicId: str 
    activityId: str 
    actionType: int
    productInOutType: int
    speed: Optional[float] = None
    productCount: int
    useProductCheck: bool
    pioSideType: int
    pioComType: int
    pioId: Optional[str] = None
    pioChannel: Optional[int] = None
    class Config:
        extra = 'forbid'


# LiftActivity
class ExpectedLiftActivity(BaseModel):
    topicId: str 
    activityId: str 
    height: int
    speed: Optional[float] = None
    useProductCheck: bool
    class Config:
        extra = 'forbid'


# ChargeStartActivity
class ExpectedChargeStartActivity(BaseModel):
    topicId: str 
    activityId: str 
    pioSideType: int
    pioComType: int
    pioId: Optional[str] = None
    pioChannel: Optional[int] = None
    ignoreFail: Optional[bool] = None
    class Config:
        extra = 'forbid'


# ChargeStopActivity
class ExpectedChargeStopActivity(BaseModel):
    topicId: str 
    activityId: str
    class Config:
        extra = 'forbid' 


# TableTurnActivity
class ExpectedTableTurnActivity(BaseModel):
    topicId: str 
    activityId: str 
    targetAngle: float
    speed: float
    class Config:
        extra = 'forbid'


# ControlPtzActivity
class ExpectedControlPtzActivity(BaseModel):
    topicId: str 
    activityId: str 
    pan: float
    tilt: float
    zoom: int
    class Config:
        extra = 'forbid'


# GetPictureActivity
class ExpectedGetPictureActivity(BaseModel):
    topicId: str 
    activityId: str 
    camId: int
    photoNum: int
    interval: int
    saveLocal: Optional[bool] = None
    description: Optional[str] = None
    uploadServer: Optional[bool] = None
    directoryName: str
    nodeName: str
    class Config:
        extra = 'forbid'


# UploadRequestActivity
class ExpectedUploadRequestActivity(BaseModel):
    topicId: str 
    activityId: str 
    url: str
    directoryName: str
    class Config:
        extra = 'forbid'


# SetSound
class ExpectedSetSound(BaseModel):
    topicId: str 
    pattern: int 
    class Config:
        extra = 'forbid'


# SetLed
class ExpectedUSetLed(BaseModel):
    topicId: str 
    pattern: int 
    class Config:
        extra = 'forbid'



