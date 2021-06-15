## Search queries
### Search 1
db.reuters.find(
	{
		$and:
		[
			{"PLACES.D":"indonesia"},
            {"TOPICS.D":"sugar"}
		]
	}
).pretty();

### Search 2
db.reuters.find(
	{
		$text:
		{
			$search:"colombia and coffee"
		}
	}
).pretty();

## Aggregation queries
db.reuters.aggregate(
    [
        {$unwind:"$PLACES.D"},
        {
            $group:
            {
                "_id":"$PLACES.D",
                "count":{$sum:1}
            }
        },
        {
            $sort: {
                "_id":1
            }
        },
        {
            $group:
            {
                "_id":null,
                "countries":
                {
                    $push:
                    {"_id":"$_id",
                    "value":"$count"
                    }
                }
            }
        },
        {
            $project:
            {
                "_id":0,
                "countries":1
            }
        },
    ]
).pretty();