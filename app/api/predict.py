import logging
import random

from fastapi import APIRouter

import pandas as pd

from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)

router = APIRouter()


class Item(BaseModel):
    """Use this data model to parse the request body JSON."""

    user : str = Field(..., example='H@xx')
    comment_id : int = Field(..., example=9360)
    text : str = Field(..., example='Apple is cool.')

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

    @validator('comment_id')
    def comment_id_must_be_positive(cls, value):
        """Validate that comment_id is a positive number."""
        assert value > 0, f'comment_id == {value}, must be > 0'
        return value


@router.post('/predict')
async def predict(item: Item):
    """Make random baseline predictions for classification problem."""
    X_new = item.to_df()
    log.info(X_new)
    y_pred = random.choice(["Salty", "Not Salty"])
    y_pred_proba = random.random() / 2 + 0.5
    return {
        'prediction': y_pred,
        'probability': y_pred_proba
    }
