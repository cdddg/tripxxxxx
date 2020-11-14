from orm import tour


def get_tour_groups_rows(order_by_field=None, sort_type=None):
    # query = f'''
    #     SELECT
    #         TOUR_GROUP.*,
    #         BUCKET.*,
    #         BUCKET.adult_price as `price`
    #     FROM
    #         {tour.models.TourGroupBase._meta.db_table} as `TOUR_GROUP`
    #     LEFT JOIN (
    #             SELECT * FROM {tour.models.TourGroupBucket._meta.db_table} WHERE date = date(now())
    #         ) as `BUCKET` on BUCKET.tour_group_id = TOUR_GROUP.id

    # '''

    query = f"""
        SELECT
            *
        FROM
            {tour.models.TourGroupBase._meta.db_table} as `TOUR_GROUP`
        JOIN (
            SELECT
                *
            FROM (
                SELECT
                    id,
                    tour_group_id,
                    date,
                    sku,
                    sell,
                    adult_price as `price`,
                    adult_price,
                    child_price,
                    baby_price,
                    remark
                FROM
                    {tour.models.TourGroupBucket._meta.db_table}
                WHERE
                     date >= date(now()) and sku > sell
                ORDER BY
                    date
                ) as `_BUCKET`
            GROUP BY
                tour_group_id
            ) as `BUCKET` on BUCKET.tour_group_id = TOUR_GROUP.id
        {f'ORDER BY {order_by_field} {sort_type}' if all([order_by_field, sort_type]) else ''}
        ;
    """
    return query
