Feature: Show User our catalog of books with a paginated view

  Scenario: The Bookstore Catalog opens with the Default view
    Given a catalog with at least 1 book
    When I open the catalog
    Then I start on Page 1 which shows the first (up to) 10 books

  Scenario: Navigate through Pagination when there are more than 10 books
    Given a catalog with more than 10 books
    When I click Next
    Then I should see Page 2 with books 11 through 20