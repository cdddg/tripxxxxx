from orm import tour


def get_tour_groups_rows(order_by_field=None, sort_type=None):
    query = f'''
        SELECT
            TOUR_GROUP.*,
            BUCKET.*,
            BUCKET.adult_price as `price`
        FROM
            {tour.models.TourGroupBase._meta.db_table} as `TOUR_GROUP`
        LEFT JOIN (
                SELECT * FROM {tour.models.TourGroupBucket._meta.db_table} WHERE date = date(now())
            ) as `BUCKET` on BUCKET.tour_group_id = TOUR_GROUP.id
    '''

    if all([order_by_field, sort_type]):
        if order_by_field == 'price':
            _condition = f'IFNULL(price, default_price) {sort_type}'
        else:
            _condition = f'{order_by_field} {sort_type}'

        query += f'''
            ORDER BY {_condition}
        '''

    return query + ';'
