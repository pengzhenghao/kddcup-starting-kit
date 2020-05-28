# -*- coding: utf-8 -*-
# @File: agent.py
# @Author: Xiaocheng Tang
# @Date:   2020-03-17 17:03:34
import random


class Agent(object):
    """ Agent for dispatching and reposition """

    def __init__(self):
        """ Load your trained model and initialize the parameters """
        pass

    def dispatch(self, dispatch_observ):
        """ Compute the assignment between drivers and passengers at each
        time step
        :param dispatch_observ: a list of dict, the key in the dict includes:
            order_id, int
            driver_id, int
            order_driver_distance, float
            order_start_location, a list as [lng, lat], float
            order_finish_location, a list as [lng, lat], float
            driver_location, a list as [lng, lat], float
            timestamp, int
            order_finish_timestamp, int
            day_of_week, int
            reward_units, float
            pick_up_eta, float

        :return: a list of dict, the key in the dict includes:
            order_id and driver_id, the pair indicating the assignment
        """
        order_ids = list(set(obs["order_id"] for obs in dispatch_observ))
        driver_ids = list(set(obs["driver_id"] for obs in dispatch_observ))
        dispatch_action = [
            dict(order_id=order_id, driver_id=random.choice(driver_ids))
            for order_id in order_ids
        ]
        return dispatch_action

    def reposition(self, repo_observ):
        """ Compute the reposition action for the given drivers
        :param repo_observ: a dict, the key in the dict includes:
            timestamp: int
            driver_info: a list of dict, the key in the dict includes:
                driver_id: driver_id of the idle driver in the treatment
                group, int
                grid_id: id of the grid the driver is located at, str
            day_of_week: int

        :return: a list of dict, the key in the dict includes:
            driver_id: corresponding to the driver_id in the od_list
            destination: id of the grid the driver is repositioned to, str
        """
        repo_action = []
        for driver in repo_observ['driver_info']:
            # the default reposition is to let drivers stay where they are
            repo_action.append(
                {
                    'driver_id': driver['driver_id'],
                    'destination': driver['grid_id']
                }
            )
        return repo_action
