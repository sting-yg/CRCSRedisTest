from typing import List, Optional
from pydantic import BaseModel


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



# vmarker
class ExpectedVmarker(BaseModel):
    x: float
    y: float


# docking method value
class ExpectedDockingMethodValue(BaseModel):
    # slam: Optional[str] = None
    vmarker: List[ExpectedVmarker]
    # qr: Optional[str] = None
    # qrStrip: Optional[str] = None
    # arucoMarker: Optional[bool] = None


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


# Move
class ExpectedMoveActivity(BaseModel):
    topicId: str 
    activityId: str 
    driveType: int
    doAlign: Optional[bool] = None
    alignAngle: Optional[float] = None
    pathList: List[ExpectedMovePath]
    


# Docking
class ExpectedDockingActivity(BaseModel):
    topicId: str 
    inOutType: int 
    activityId: str 
    pathList: List[ExpectedDockingPath]


# KivaTurn
class ExpectedKivaTurnActivity(BaseModel):
    topicId: str 
    activityId: str 
    targetAngle: int
    speed: int


# Cancel
class ExpectedCancelActivity(BaseModel):
    topicId: str
    stopAtNode: Optional[bool] = None


# Pause
class ExpectedPause(BaseModel):
    topicId: str


# Resume
class ExpectedResume(BaseModel):
    topicId: str


# SpeedControl
class ExpectedSpeedControl(BaseModel):
    topicId: str 
    speed: float


# DriveJog
class ExpectedDriveJog(BaseModel):
    topicId: str
    linearXVelocity: float
    linearYVelocity: Optional[float] = None
    angularVelocity: float


# AlarmClear
class ExpectedAlarmClear(BaseModel):
    topicId: str


# SetMap
class ExpectedSetMap(BaseModel):
    topicId: str
    filePath: str


# InitPose
class ExpectedInitPose(BaseModel):
    topicId: str
    x: float
    y: float
    angle: float


# Heartbeat
class ExpectedInitPose(BaseModel):
    topicId: str


# Error
class ExpectedError(BaseModel):
    code: int
    message: str


# Event
# AlarmOccurred
class ExpectedAlarmOccurred(BaseModel):
    topicId: str
    error: list[ExpectedError]


# NavigationStatus
class ExpectedNavigationStatus(BaseModel):
    topicId: str
    x: float
    y: float
    angle: float
    linearXVelocity: float
    linearYVelocity: float
    angularVelocity: float
    state: int
    mapConfidence: float
    obstacleDetected: int
    mapVersion: str
    version: str


# NavigationMileage
class ExpectedNavigationMileage(BaseModel):
    topicId: str
    driveMileage: Optional[float] = None
    driveTime: Optional[float] = None


# Error
class ExpectedPoint(BaseModel):
    x: float
    y: float


# LidarStatus
class ExpectedLidarStatus(BaseModel):
    topicId: str
    cordinateType: int
    point: list[ExpectedPoint]


# CameraStatus
class ExpectedCameraStatus(BaseModel):
    topicId: str
    cordinateType: int
    point: list[ExpectedPoint]



