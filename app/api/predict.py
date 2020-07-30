import logging

from fastapi import APIRouter

import pandas as pd

from pydantic import BaseModel, Field, validator

from .model import *

log = logging.getLogger(__name__)

router = APIRouter()



class Item(BaseModel):
    """Use this data model to parse the request body JSON."""

    
    comment_id : int = Field(..., example=23970146)
    #user_name : str = Field(..., example='gmfawcett')
    #comment_id_list : list = Field(..., example=[23970146,457634])

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

    @validator('comment_id')
    def comment_id_must_be_positive(cls, value):
        """Validate that comment_id is a positive number."""
        assert value > 0, f'comment_id == {value}, must be > 0'
        return value


@router.get('/saltiest100')
def print_saltiest():
    l_pred = get_scores_by_user()
    return {
        'Top_100_Saltiest': l_pred
        }

@router.post('/predict')
async def predict(item: Item):
    """Make random baseline predictions for classification problem."""
    X_new = item.to_df()
    log.info(X_new)
    
    y_pred = get_score_by_comment_id(item.comment_id)
    #U_pred = get_cummulative_score_for_user(item.user_name)
    #l_pred = get_scores_by_user()
    return {
        
        'Score_for_comment_from_id': y_pred,
        #'user cumulative comment score': U_pred,
        #'Score for list of comment ids': l_pred
    }
