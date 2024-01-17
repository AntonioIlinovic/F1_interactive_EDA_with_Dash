import dash
from dash import Output, Input

from common.utils.utils import get_dataset_columns
from pages.distribution_histogram.data import get_histogram_distribution


@dash.callback(
    Output('distribution-histogram-column-dropdown', 'options'),
    Input('distribution-histogram-dataset-dropdown', 'value')
)
def update_distribution_column_name_dropdown_options(dataset_name):
    df_columns = get_dataset_columns(dataset_name)
    values_for_dataset_dropdown = [{'label': column_name, 'value': column_name}
                                   for column_name in df_columns]

    return values_for_dataset_dropdown


@dash.callback(
    Output('distribution-histogram', 'figure'),
    [Input('distribution-histogram-dataset-dropdown', 'value'),
     Input('distribution-histogram-column-dropdown', 'value')]
)
def update_distribution_histogram(dataset_name, column_name):

    # TODO refactor code

    return get_histogram_distribution(dataset_name, column_name)
