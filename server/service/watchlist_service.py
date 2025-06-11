from repository import (insert_one_table,
                        remove_from_one_table,
                        latest_trade_day_entry,
                        watchlist_overview,
                        update_single_stock_datas)


def load_watchlist(customer_id):

    result = watchlist_overview(customer_id)

    return result


def editing_watchlist(customer_id, add, to_eddit: dict):

    to_eddit["customer_id"] = customer_id

    if add is False:
        remove_from_one_table("watchlist", to_eddit)

    else:
        update_single_stock_datas(to_eddit["isin"])
        result = latest_trade_day_entry(to_eddit["isin"])
        to_eddit["price"] = result["close"]

        insert_one_table("watchlist", to_eddit)


if __name__ == "__main__":

    test = {"isin": "DE000SYM9999"}

    answer = editing_watchlist(1, test)

    print("answer", answer)
