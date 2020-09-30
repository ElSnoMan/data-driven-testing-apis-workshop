Feature: Display the books in a Table with the correct information
  The user can edit number of rows displayed and sort books by column,
  but the info we need displayed is:
  1. Image
  2. Title
  3. Author
  4. Publisher

  Background:
    Given a catalog with these books:
	  | Image | Title | Author | Publisher |
	  | 0.jpg | Git Pocket Guide | Richard E. Silverman | O'Reilly Media |
	  | 1.jpg | Learning JavaScript Design Patterns | Addy Osmani | O'Reilly Media |
	  | 2.jpg | Designing Evolvable Web APIs with ASP | Glenn Block et al | O'Reilly Media |
	  | 3.jpg | Speaking JavaScript | Axel Rauschmayer | O'Reilly Media |
	  | 4.jpg | You Don't Know JS | Kyle Simpson | O'Reilly Media |
	  | 5.jpg | Programming JavaScript Applications | Eric Elliot | O'Reilly Media |
	  | 6.jpg | Eloquent JavaScript, Second Edition | Marijn Haverbeke | No Starch Press |
	  | 7.jpg | Understanding ECMAScript 6 | Nicholas C. Zakas | No Starch Press |

  Scenario: Books have an Image, Title, Author and Publisher
	When I open the catalog
	Then I should see 8 books
	And each book should have a value for Image, Title, Author and Publisher

  Scenario Outline: User can change the number of rows to see in a single page
	When I open the catalog
	And change the number of rows to <amount> rows
	Then I should see <amount> rows

	Examples:
	  | amount |
	  | 5 |
	  | 20 |
	  | 25 |
	  | 50 |
	  | 100 |