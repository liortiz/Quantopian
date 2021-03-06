# -*- coding: utf-8 -*-
"""liortiz Getting Started: Lesson 5 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FU5lvsZQqMMP1AF-_7fqQiqch0eDf2eO
"""

# Import Algorithm API
import quantopian.algorithm as algo


def initialize(context):
    # Initialize algorithm parameters
    context.day_count = 0
    context.daily_message = "Day {}."
    context.weekly_message = "Time to place some trades!"

    # Schedule rebalance function
    algo.schedule_function(
        rebalance,
        date_rule=algo.date_rules.week_start(),
        time_rule=algo.time_rules.market_open()
    )


def before_trading_start(context, data):
    # Execute any daily actions that need to happen
    # before the start of a trading session
    context.day_count += 1
    log.info(context.daily_message, context.day_count)


def rebalance(context, data):
    # Execute rebalance logic
    log.info(context.weekly_message)