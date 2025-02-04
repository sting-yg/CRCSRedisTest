from typing import List, Optional
from pydantic import BaseModel


class ExpectedPathStructure(BaseModel):
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
    

# Move
class ExpectedMoveActivity(BaseModel):
    topicId: str 
    activityId: str 
    driveType: int
    doAlign: Optional[bool] = None
    alignAngle: Optional[float] = None
    pathList: List[ExpectedPathStructure]
    

# Docking
class ExpectedDockingActivity(BaseModel):
    topicId: str 
    inOutType: int 
    activityId: str 
    pathList: List[ExpectedPathStructure]


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
    linearXVelocity: Optional[float] = None
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

