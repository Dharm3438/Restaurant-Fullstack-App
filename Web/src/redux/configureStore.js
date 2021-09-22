import {createStore, combineReducers} from 'redux';
import { Dishes } from './red_dishes';
import { Comments } from './red_comments';
import { Promotions } from './red_promotions';
import { Leaders } from './red_leaders';

export const ConfigureStore = () => {
    const store = createStore(
        combineReducers({
            dishes: Dishes,
            comments: Comments,
            promotions: Promotions,
            leaders: Leaders
        })
    );

    return store;
}