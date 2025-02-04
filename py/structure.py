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
    driveType: int
    pathList: List[ExpectedPathStructure]
    doAlign: Optional[bool] = None
    alignAngle: Optional[float] = None


class ExpectedDockingParameter(BaseModel):
    driveType: int
    pathList: List[ExpectedPathStructure]


class ExpectedConveyorParameter(BaseModel):
    actionType: int
    productInOutType: int
    speed: int
    productCount: int
    useProductCheck: bool
    pioSideType: int
    pioComType: int
    pioId: str
    pioChannel: int


class ExpectedStandbyParameter(BaseModel):
    seconds: int
    useBatterySaving: bool


class ExpectedChargeStartParameter(BaseModel):
    pioSideType: int
    pioComType: int
    pioId: str
    pioChannel: int
    ignoreFail: bool


class ExpectedTableTurnParameter(BaseModel):
    targetAngle: float
    speed: float


class ExpectedKivaTurnParameter(BaseModel):
    targetAngle: float
    speed: float


class ExpectedLiftParameter(BaseModel):
    actionType: int
    height: float
    speed: float
    useProductCheck: bool


class ExpectedControlPTZParameter(BaseModel):
    pan: float
    tilt: float
    zoom: float


class ExpectedGetPictureParameter(BaseModel):
    camId: int
    photoNum: int
    interval: int
    saveLocal: bool
    description: str
    uploadServer: bool
    directoryName: str
    nodeName: str


class ExpectedUploadRequestParameter(BaseModel):
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
    repeatCount: int
