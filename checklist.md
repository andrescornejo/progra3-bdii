# Progra 3 bdii checklist
- [x] convert xml to json
- [x] load json into the mongo db
- [x] index the data
- [x] data search
- [x] Aditional operations

## notes
- xml has characters that do not conform to the standard, so they are impossible to convert without tinkering.
- Solution was to change all the instances of &# to @0@
- Since all of the objects inside the "REUTERS" array in the json need to be inserted as separate documents, the files have to be modified to be json arrays
- Once the files are in a json array use the *mongoimport* tool
    - The command used to import is: ```mongoimport --db test --collection example --type json --file example.json --jsonArray```

## Other code that contributed to success.
{"PLACES.D":"indonesia"}
{"TOPICS.D":"sugar"}

{$text:{$search:"colombia and coffee"}}

db.reuters.aggregate(
    [
        {
            $group:
            {
                _id:null,
                value: {$push: { item: "$PLACES.D", num:{$sum:"$PLACES.D"}}},
            }

        }
    ]
);

db.reuters.aggregate(
    [
        {
            $group:
            {
                _id: {$push: {"$PLACES.D"}}
            }

        }
    ]
);

db.reuters.aggregate([
    {$group: {_id:"$PLACES.D",
                value:{$sum:1}}}
]);

db.reuters.aggregate([
    {$group: 
        {_id: {$push: {_id: "$PLACES.D"},
                value:{$sum:1}}}} ]);

db.reuters.aggregate(
    [
        {
            $group:
            {
                _id:null,
                value: {$push: "$PLACES.D"}
            }

        }
    ]
);