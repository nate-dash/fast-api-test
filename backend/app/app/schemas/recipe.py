from pydantic import ConfigDict, BaseModel, HttpUrl

from typing import Sequence


class RecipeBase(BaseModel):
    label: str
    source: str
    url: HttpUrl


class RecipeCreate(RecipeBase):
    label: str
    source: str
    url: HttpUrl
    submitter_id: int


class RecipeUpdate(RecipeBase):
    id: int


class RecipeUpdateRestricted(BaseModel):
    id: int
    label: str


# Properties shared by models stored in DB
class RecipeInDBBase(RecipeBase):
    id: int
    submitter_id: int
    model_config = ConfigDict(from_attributes=True)


# Properties to return to client
class Recipe(RecipeInDBBase):
    pass


# Properties properties stored in DB
class RecipeInDB(RecipeInDBBase):
    pass


class RecipeSearchResults(BaseModel):
    results: Sequence[Recipe]
