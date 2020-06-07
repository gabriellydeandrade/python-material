from behave import *

from create_list import create_list


@when("a new list is created")
def step_new_list(context):
    context.result = create_list()


@then("the list should be empty.")
def step_new_list(context):
    assert bool(context.result) is False


@when("a new list is created passing an element")
def step_new_list(context):
    context.result = create_list(element=1)


@then("the list should not be empty.")
def step_new_list(context):
    assert bool(context.result) is not False
