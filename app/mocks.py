FASTAPI_MOCKED_BOOKS = [
    {
        'author': 'Richard E. Silverman',
        'image': '0.jpg',
        'isbn': '9781449325862',
        'publisher': "O'Reilly Media",
        'title': 'Git Pocket Guide'
    },
    {
        'author': 'Addy Osmani',
        'image': '1.jpg',
        'isbn': '9781449331818',
        'publisher': "O'Reilly Media",
        'title': 'Learning JavaScript Design Patterns'
    },
    {
        'author': 'Glenn Block et al.',
        'image': '2.jpg',
        'isbn': '9781449337711',
        'publisher': "O'Reilly Media",
        'title': 'Designing Evolvable Web APIs with ASP.NET'
    },
    {
        'author': 'Axel Rauschmayer',
        'image': '3.jpg',
        'isbn': '9781449365035',
        'publisher': "O'Reilly Media",
        'title': 'Speaking JavaScript'
    },
    {
        'author': 'Kyle Simpson',
        'image': '4.jpg',
        'isbn': '9781491904244',
        'publisher': "O'Reilly Media",
        'title': "You Don't Know JS"
    },
    {
        'author': 'Eric Elliott',
        'image': '5.jpg',
        'isbn': '9781491950296',
        'publisher': "O'Reilly Media",
        'title': 'Programming JavaScript Applications'
    },
    {
        'author': 'Marijn Haverbeke',
        'image': '6.jpg',
        'isbn': '9781593275846',
        'publisher': 'No Starch Press',
        'title': 'Eloquent JavaScript, Second Edition'
    },
    {
        'author': 'Nicholas C. Zakas',
        'image': '7.jpg',
        'isbn': '9781593277574',
        'publisher': 'No Starch Press',
        'title': 'Understanding ECMAScript 6'
    }
]


FASTAPI_MOCKED_INVALID_BOOKS = [
    {
        # missing author
        'image': '0.jpg',
        'isbn': '9781449325862',
        'publisher': "O'Reilly Media",
        'title': 'Git Pocket Guide'
    },
    {
        'author': 'Addy Osmani',
        # missing image
        'isbn': '9781449331818',
        'publisher': "O'Reilly Media",
        'title': 'Learning JavaScript Design Patterns'
    },
    {
        'author': 'Glenn Block et al.',
        'image': '2.jpg',
        # isbn is number instead of string
        'isbn': 9,
        'publisher': "O'Reilly Media",
        'title': 'Designing Evolvable Web APIs with ASP.NET'
    },
    {
        'author': 'Axel Rauschmayer',
        'image': '3.jpg',
        'isbn': '9781449365035',
        # publisher is None instead of string
        'publisher': None,
        'title': 'Speaking JavaScript'
    },
    {
        # empty dictionary
    }
]
