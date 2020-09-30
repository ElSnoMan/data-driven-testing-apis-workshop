Feature: Users can add books to their Collection if they are logged in

  Scenario: Guest tries to add books while not logged in
    Given the guest is not logged in
    When they try to add a book to their collection
    Then a login prompt appears

  Scenario: User adds a book to their collection
    Given a logged in user
    When they add a book to their collection
    Then they should see an "Added" message
    And have the book in their collection