from typing import List, Optional
from pydantic import BaseModel

# vmarker
class ExpectedVmarker(BaseModel):
    x: float
    y: float
    class Config:
        extra = "ignore"


# docking method value
class ExpectedDockingMethodValue(BaseModel):
    # slam: Optional[str] = None
    vmarker: List[ExpectedVmarker]
    # qr: Optional[str] = None
    # qrStrip: Optional[str] = None
    # arucoMarker: Optional[bool] = None
    class Config:
        extra = "ignore"
class ExpectedPathStructure(BaseModel):
    index: int
    # node: str #croa.core
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
    trafficGrantStop: Optional[bool] = None # ??
    isNeedStop: Optional[bool] = None # ??
    dockingMinLinearVel: Optional[str] = None # ??
    dockingSpeedReduceRate: Optional[float] = None # ??
    class Config:
        extra = "ignore"


class ExpectedMoveParameter(BaseModel):
    # topicId: str #croa.core
    # activityId: str #croa.core
    driveType: int
    pathList: List[ExpectedPathStructure]
    doAlign: Optional[bool] = None
    alignAngle: Optional[float] = None
    class Config:
        extra = "ignore"


class ExpectedDockingParameter(BaseModel):
    # topicId: str #croa.core
    # activityId: str #croa.core
    # inOutType: int #croa.core
    driveType: int # ??
    pathList: List[ExpectedPathStructure]
    class Config:
        extra = "ignore"


class ExpectedKivaTurnParameter(BaseModel):
    # topicId: str #croa.core
    # activityId: str #croa.core
    targetAngle: float
    speed: float
    class Config:
        extra = "ignore"


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


class ExpectedLiftParameter(BaseModel):
    # topicId: str #croa.core
    # activityId: str #croa.core
    actionType: int # ??
    # height: float #croa.core
    speed: float
    useProductCheck: bool
    class Config:
        extra = "ignore"


class ExpectedStandbyParameter(BaseModel):
    seconds: int
    useBatterySaving: bool
    class Config:
        extra = "ignore"


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


class ExpectedTableTurnParameter(BaseModel):
    # topicId: str #croa.core
    # activityId: str #croa.core
    targetAngle: float
    speed: float
    class Config:
        extra = "ignore"


class ExpectedControlPTZParameter(BaseModel):
    # topicId: str #croa.core
    # activityId: str #croa.core
    pan: float
    tilt: float
    zoom: int
    class Config:
        extra = "ignore"


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


class ExpectedUploadRequestParameter(BaseModel):
    # topicId: str #croa.core
    # activityId: str #croa.core
    url: str
    directoryName: str
    class Config:
        extra = "ignore"


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
