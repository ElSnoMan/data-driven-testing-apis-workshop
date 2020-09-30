Feature: Users can filter the list of books with a Search
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

  Scenario Outline: User enters an exact search
    When I search <query>
    Then I should see <result> book(s)

	Examples:
	  | query | result |
	  | "Git Pocket Guide" | 1 |
	  | "eric elliot" | 1 |
	  | "O'Reilly Media" | 6 |
	  | "Carlos Kidman" | 0 |

  Scenario Outline: User enters a fuzzy search
    When I search <query>
    Then I should see <result> book(s) with the term somewhere in Title, Author, or Publisher

	Examples:
	  | query | result |
	  | javascript | 4 |
	  | a | 8 |
	  | as | 6 |
	  | asf | 0 |