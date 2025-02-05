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


class ExpectedMoveParameter(BaseModel):
    # topicId: str #croa.core
    # activityId: str #croa.core
    driveType: int
    pathList: List[ExpectedPathStructure]
    doAlign: Optional[bool] = None
    alignAngle: Optional[float] = None


class ExpectedDockingParameter(BaseModel):
    # topicId: str #croa.core
    # activityId: str #croa.core
    # inOutType: int #croa.core
    driveType: int # ??
    pathList: List[ExpectedPathStructure]


class ExpectedKivaTurnParameter(BaseModel):
    # topicId: str #croa.core
    # activityId: str #croa.core
    targetAngle: float
    speed: float


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


class ExpectedLiftParameter(BaseModel):
    # topicId: str #croa.core
    # activityId: str #croa.core
    actionType: int # ??
    height: float
    speed: float
    useProductCheck: bool


class ExpectedStandbyParameter(BaseModel):
    seconds: int
    useBatterySaving: bool


class ExpectedChargeStartParameter(BaseModel):
    # topicId: str #croa.core
    # activityId: str #croa.core
    pioSideType: int
    pioComType: int
    pioId: Optional[str] = None
    pioChannel: Optional[int] = None
    ignoreFail: Optional[bool] = None


class ExpectedTableTurnParameter(BaseModel):
    # topicId: str #croa.core
    # activityId: str #croa.core
    targetAngle: float
    speed: float


class ExpectedControlPTZParameter(BaseModel):
    # topicId: str #croa.core
    # activityId: str #croa.core
    pan: float
    tilt: float
    zoom: int


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


class ExpectedUploadRequestParameter(BaseModel):
    # topicId: str #croa.core
    # activityId: str #croa.core
    url: str
    directoryName: str


class ExpectedActivityStructure(BaseModel):
    activityType: int
    index: int
    id: Optional[str] = None
    isAsync: bool
    isTaskOverridable: bool
    palletSize: Optional[int] = None
    palletHeight: int
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
    visible: bool


class ExpectedTaskStructure(BaseModel):
    taskInstanceId: str
    requesterId: Optional[str] = None
    requesterName: Optional[str] = None
    requesterOrganizationName: Optional[str] = None
    startNodeName: Optional[str] = None
    targetNodeName: Optional[str] = None
    alias: str
    activities: List[ExpectedActivityStructure]
    # repeatCount: int
