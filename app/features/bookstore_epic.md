# EPIC: Bookstore Category
Create a Bookstore Catalog for Shoppers to browse through.

## Acceptance Criteria

* Show User our catalog of books with a paginated view
* Users can filter the list of books with a Search
* Users can add books to their Collection if they are logged in
* The data to show for each book is (in order from left to right):
	1. Image
	2. Title
    3. Author
    4. Publisher
    
## Technical Design

BookModel

```javascript
{
    "author": string,
    "image": string,
    "isbn": string,
    "publisher": string,
    "title": string
}
```

