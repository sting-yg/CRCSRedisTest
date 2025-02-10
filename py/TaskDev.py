from typing import List, Optional
from pydantic import BaseModel


# ✅❎
# vmarker
class ExpectedVmarker(BaseModel):
    x: float
    y: float
    class Config:
        extra = "ignore"


# docking method value
class ExpectedDockingMethodValue(BaseModel):
    vmarker: List[ExpectedVmarker]
    class Config:
        extra = "ignore"


# path
class ExpectedPathStructure(BaseModel):
    index: int
    # node: str # 문서 (유) Dev(무)
    x: float
    y: float
    angle: float
    actionType: int
    isArc: bool
    arcRadius: float
    arcControlPointX: Optional[float] = None
    arcControlPointY: Optional[float] = None
    speed: float
    obstacleDetectionDistance: Optional[List[float]] = None
    obstacleDetectionAreaAtTarget: Optional[List[float]] = None
    dockingMethodType: Optional[int] = None
    dockingMethodValue: Optional[ExpectedDockingMethodValue] = None
    trafficGrantStop: Optional[bool] = None # 문서 (무) Dev (유)
    isNeedStop: Optional[bool] = None # 문서 (무) Dev (유)
    dockingMinLinearVel: Optional[str] = None # 문서 (무) Dev (유)
    dockingSpeedReduceRate: Optional[float] = None # 문서 (무) Dev (유)
    class Config:
        extra = "ignore"



# move
class ExpectedMoveParameter(BaseModel):
    # topicId: str #croa.core  # 문서 (유) Dev(무)
    # activityId: str #croa.core # 문서 (유) Dev(무)
    driveType: int
    doAlign: Optional[bool] = None
    alignAngle: Optional[float] = None
    pathList: List[ExpectedPathStructure]
    
    class Config:
        extra = "ignore"



# docking
class ExpectedDockingParameter(BaseModel):
    # topicId: # 문서 (유) Dev(무)
    # inOutType: # 문서 (유) Dev(무)
    # activityId: # 문서 (유) Dev(무)
    driveType: int # 문서 (무) Dev(유유)
    pathList: List[ExpectedPathStructure]
    class Config:
        extra = "ignore"



# kivaTurn
class ExpectedKivaTurnParameter(BaseModel):
    # topicId: str #croa.core
    # activityId: str #croa.core
    targetAngle: float
    speed: float
    class Config:
        extra = "ignore"



# conveyor
class ExpectedConveyorParameter(BaseModel):
    # topicId: str #croa.core
    # activityId: str #croa.core
    actionType: int
    productInOutType: int
    speed: Optional[int] = None
    productCount: int
    useProductCheck: bool
    pioSideType: int
    pioComType: int
    pioId: Optional[str] = None
    pioChannel: Optional[int] = None
    class Config:
        extra = "ignore"



# lift
class ExpectedLiftParameter(BaseModel):
    # topicId: # 문서(유) Dev(무)
    # activityId: # 문서(유) Dev(무)
    actionType: int # 문서(무) Dev(유유)
    # height: float # 문서(유) Dev(무)
    speed: Optional[float] = None
    useProductCheck: bool
    class Config:
        extra = "ignore"



# standby
class ExpectedStandbyParameter(BaseModel):
    seconds: int
    useBatterySaving: bool
    class Config:
        extra = "ignore"



# chargeStart
class ExpectedChargeStartParameter(BaseModel):
    # topicId: str #croa.core
    # activityId: str #croa.core
    pioSideType: int
    pioComType: int
    pioId: Optional[str] = None
    pioChannel: Optional[int] = None
    ignoreFail: Optional[bool] = None
    class Config:
        extra = "ignore"



# tableTurn
class ExpectedTableTurnParameter(BaseModel):
    # topicId: str #croa.core
    # activityId: str #croa.core
    targetAngle: float
    speed: float
    class Config:
        extra = "ignore"



# PTZ 
class ExpectedControlPTZParameter(BaseModel):
    # topicId: str #croa.core
    # activityId: str #croa.core
    pan: float
    tilt: float
    zoom: int
    class Config:
        extra = "ignore"



# getPicture
class ExpectedGetPictureParameter(BaseModel):
    # topicId: str #croa.core
    # activityId: str #croa.core
    camId: int
    photoNum: int
    interval: int
    saveLocal: Optional[bool] = None
    description: Optional[str] = None
    uploadServer: Optional[bool] = None
    directoryName: str
    nodeName: str
    class Config:
        extra = "ignore"



# uploadRequest
class ExpectedUploadRequestParameter(BaseModel):
    # topicId: str #croa.core
    # activityId: str #croa.core
    url: str
    directoryName: str
    class Config:
        extra = "ignore"



# activity
class ExpectedActivityStructure(BaseModel):
    activityType: int
    index: int
    id: Optional[str] = None
    isAsync: bool
    isTaskOverridable: bool
    palletSize: Optional[int] = None
    palletHeight: Optional[int] = None
    moveParameter: Optional[ExpectedMoveParameter] = None
    dockingInParameter: Optional[ExpectedDockingParameter] = None
    dockingOutParameter: Optional[ExpectedDockingParameter] = None
    conveyorParameter: Optional[ExpectedConveyorParameter] = None
    standbyParameter: Optional[ExpectedStandbyParameter] = None
    chargeStartParameter: Optional[ExpectedChargeStartParameter] = None
    tableTurnParameter: Optional[ExpectedTableTurnParameter] = None
    kivaTurnParameter: Optional[ExpectedKivaTurnParameter] = None
    liftParameter: Optional[ExpectedLiftParameter] = None
    controlPtzParameter: Optional[ExpectedControlPTZParameter] = None
    getPictureParameter: Optional[ExpectedGetPictureParameter] = None
    uploadRequestParameter: Optional[ExpectedUploadRequestParameter] = None
    visible: bool # ??
    class Config:
        extra = "ignore"



# task
class ExpectedTaskStructure(BaseModel):
    taskInstanceId: str
    requesterId: Optional[str] = None
    requesterName: Optional[str] = None
    requesterOrganizationName: Optional[str] = None
    startNodeName: Optional[str] = None
    targetNodeName: Optional[str] = None
    alias: str
    activities: List[ExpectedActivityStructure]
    repeatCount: int # ??
    class Config:
        extra = "ignore"
