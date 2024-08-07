# Performance Footwear

Welcome to Performance Footwear. This website is aimed at users who have a passion for running and the latest running shoes and accessories on the market. 
The site offers exclusive features for users that have an account with us, these include adding items to your wishlist to purchase in the future, viewing your order history, saving delivery preferences and adding reviews to products.
Users who visit the site are met with a user friendly experience, They can easily search for products, view products by category, add products to their bag/basket and make payment easily. There is also a section to send us a message, a privacy policy page and information about returning products.

[Link to Performance Footwear](https://performance-footwear-ed28bb401f1b.herokuapp.com/)

![Home Screen](documentation/readme_images/responsive.png)

<br>

# UX

## Strategy

### Target Users

- Running enthusiasts who have an active lifestyle and are interested in quality products.
- Users looking to browse and purchase running shoes and related accessories.
- Users who look for the top brands in the running shoe industry.

### Site Goals

- Allow users to view and purchase products as effortlessly as possible.
- Allow users to swiftly search for the products they like.
- Provide users with the option to create an account to store wishlist items and view orders.
- Allow users to store their preffered delivery address and be able to easily edit this.
- Offer users the ability to contact performance Footwear online.

### Peoject Goals

- Develop a fubctional e-commerce web application.
- Ensure users are met with a user-friendly interface to allow easy navigation around the site.
- Offer users a seamless shopping experience.
- Intergrate exciting features, such as a wishlist and customer reviews, enhancing CRUD functionality.

<br>

[Back to Top](#table-of-contents)

<br>

## **Agile Planning**

This project followed an agile planning approach, based on user stories. Each user story was carefully planned and included in a specific iteration.
To prioritize development tasks, each feature was catergorized as Must Have, Should Have, Could Have and Wont Have. Catergorizing each user story helped determine the importance of each feature.

View the project board [here](https://github.com/users/Marchopkins96/projects/7).

<details>
<summary> Project Board
</summary>

![Project Board](documentation/readme_images/user-stories.png)
</details>

## User Stories 

* Based on the user stories created, A project implementation plan was developed.
You can view the user stories [here](https://github.com/Marchopkins96/Performance-Footwear/issues?q=is%3Aissue+is%3Aclosed).

<details>
<summary> User Stories
</summary>

![User Stories](documentation/readme_images/issues-list.png)
</details>

* Using the MoSCoW principle (Must Have, Should Have, Could Have, Won't Have), iterations were planned for the implementation of the user stories.

View milestones [here](https://github.com/Marchopkins96/Performance-Footwear/milestones).

<details>
<summary> Milestones
</summary>

![Milestones](documentation/readme_images/iterations-list.png)
</details>

<br>

[Back to Top](#table-of-contents)

<br>

## Structure 

### Wireframes

- Wireframes have been created for all pages of the site. wireframes were crafted for mobile and desktop dimensions. [Balsamiq](https://balsamiq.com/) was employed as the tool for creating the site's wireframes.

### Home Page Wireframes

<details>
<summary>Click to View Home Page wireframes</summary>

#### Mobile
![screenshot](documentation/wireframes/wireframe-home-page-mobile-Large.png)


#### Desktop
![screenshot](documentation/wireframes/wireframe-home-page-desktop-Large.png)

</details>

### All Products Page Wireframes

<details>
<summary>Click to View All Products Page wireframes</summary>

#### Mobile
![screenshot](documentation/wireframes/wireframe-all-products-page-mobile-Large.png)


#### Desktop
![screenshot](documentation/wireframes/wireframe-all-products-page-desktop-Large.png)

</details>

### Product Detail Page Wireframes

<details>
<summary>Click to View Product Detail Page wireframes</summary>

#### Mobile
![screenshot](documentation/wireframes/wireframe-product-detail-mobile-Large.png)


#### Desktop
![screenshot](documentation/wireframes/wireframe-product-detail-desktop-Large.png)

</details>

### Basket Page Wireframes

<details>
<summary>Click to View Basket Page wireframes</summary>

#### Mobile
![screenshot](documentation/wireframes/wireframe-basket-page-mobile-Large.png)


#### Desktop
![screenshot](documentation/wireframes/wireframe-basket-page-desktop-Large.png)

</details>

### Checkout Page Wireframes

<details>
<summary>Click to View Checkout Page wireframes</summary>

#### Mobile
![screenshot](documentation/wireframes/wireframe-checkout-page-mobile-Large.png)


#### Desktop
![screenshot](documentation/wireframes/wireframe-checkout-page-desktop-Large.png)

</details>

### Contact Page Wireframes

<details>
<summary>Click to View Contact Page wireframes</summary>

#### Mobile
![screenshot](documentation/wireframes/wireframe-contact-us-mobile-Large.png)


#### Desktop
![screenshot](documentation/wireframes/wireframe-contact-us-desktop-Large.png)

</details>

### Wishlist Page Wireframes

<details>
<summary>Click to View Wishlist Page wireframes</summary>

#### Mobile
![screenshot](documentation/wireframes/wireframe-wishlist-mobile-Large.png)


#### Desktop
![screenshot](documentation/wireframes/wireframe-wishlist-desktop-Large.png)

</details>

### Edit Reviews Wireframes

<details>
<summary>Click to View Edit Reviews wireframes</summary>

#### Mobile
![screenshot](documentation/wireframes/wireframe-reviews-mobile-Large.png)


#### Desktop
![screenshot](documentation/wireframes/wireframe-reviews-desktop-Large.png)

</details>



### Database Schema 

- An entity relationship diagram (ERD) was created using [Lucid Chart](https://www.lucidchart.com/pages/tour). This allowed me to visually represent the connections between my data structures and streamlined the development. With this visual aid, it makes it much easier to understand and interact with my data.

![Database Schema](documentation/readme_images/erd-diagram.png)

[Back to Top](#table-of-contents)

<br>

## Main Plan 

- Design an inviting homepage that features eye catching images that convey the purpose of the site to the user.
- Implement user account registration to enable restricted access for editing and deleting reviews, adding products to a wishlist and saving personal user information to ensure quick and efficient checkouts.
- Develop a website that is responsive on a multitude of devices, ensuring optimum functionality across all screen sizes.
- Superusers harness the ability to create, view, update, and delete throughout the site.

<br>

# Features 

## Existing Features

### Home Page 
<details>
<summary>View home page</summary>

![Hero Image](documentation/readme_images/home-page-header.png)
</details>

- The Home page features a carousel of 3 images to instantly catch the attentions of the users visiting the site.

<br>

### Marketing Section
<details>
<summary>View marketing section</summary>

![Marketing section](documentation/readme_images/marketing-text.png)
</details>

- The marketing section is presented neatly in the middle of the homepage with more images relating to the sites purpose.
- Key words are used within the marketing text that link back to the brand name and also to aid search engine optimization.

<br>

### Footer 
<details>
<summary>View footer</summary>

![Footer](documentation/readme_images/footer.png)
</details>

- The footer is present on all pages of the site.
- It features links to contact, returns, privacy policy and links back to the home page.
- The footer also incorperates links to our MailChimp newsletter signup and a link to our FaceBook marketing page.

<details>
<summary>View subscription success</summary>

![Subscription](documentation/readme_images/subscription-success.png)
</details>

<br>

### Returns Page 
<details>
<summary>View returns page</summary>

![Returns Page Image](documentation/readme_images/returns.png)
</details>

- Information of our returns policy is provided for users who desire to return items to us.

<br>

### Contact Page
<details>
<summary>View contact page</summary>

![Contact Page Image](documentation/readme_images/contact-us.png)
</details>

- Contact information is presented in a clear and consise manner. The business phone number, address and email are displayed seperately at the top of the page.
- The page also includes a contact form enabling users to contact us. The message submitted by the user is stored in the admin panel.

<br>

### Privacy Policy
<details>
<summary>View privacy policy</summary>

![Privacy Policy Image](documentation/readme_images/privacy-policy.png)
</details>

- A privacy policy is a legal document that describes how a website collects, uses, discloses and manages the personal information of its users or customers. It contains information about the types of data collected, the purposes for collecting it, storage and security methods, and the rights of users regarding their personal information.

<br>

[Back to Top](#table-of-contents)

<br>

### Main Nav Menu
<details>
<summary>View information banners</summary>

### Free Delivery
![Nav](documentation/readme_images/free-delivery-banner.png)

### Motivational Message
![Nav](documentation/readme_images/strive-message.png)

### Free Returns
![Nav](documentation/readme_images/free-returns.png)
</details>

- Displayed at the very top of the screen, there is information for the user regarding returns and delivery, as well as a phrase of motivation for visitors to the site.


<details>
<summary>View main navigation</summary>

![Main Nav Image](documentation/readme_images/main-nav-header.png)
</details>

- Consistent throughout the site, the user will see the main navigation menu. Featuring a search bar, account/profile access, basket link with subtotal if items are in the basket, as well as links to filter products by gender, brand, type of product and sale items. When a user creates an account they will also have access to the wishlist.

<br>

### Restricted Pages
<details>
<summary>View logged in Vs logged out views for users</summary>

### Logged in view
![Logged in nav](documentation/readme_images/restricted-pages.png)

### Logged out view
![Logged out nav](documentation/readme_images/logged-out-nav.png)
</details>

- Certain pages on the site are reserved exclusively for users who are logged in. Links to the these pages appear in the Navbar when a user is logged in.
- The wishlist functionality is for users who have a registered account with us.

<br>

### Product Filtration
<details>
<summary>View product filtering</summary>

![Main-nav Dropdown](documentation/readme_images/product-filtering.png)
</details>

- Users can filter products by gender, type of product, by brand and sale items.

<details>
<summary>View sort by options</summary>

![Filter](documentation/readme_images/sort-by.png)
</details>

- When on the products page users can filter the product by price, rating, name, category and brand.

<br>

### Search Bar
<details>
<summary>View different search features</summary>

### Search Bar
![Search Bar Image](documentation/readme_images/search-bar.png)

### Product search result
![Search product](documentation/readme_images/product-search.png)

### No search results
![No result search](documentation/readme_images/no-results-search.png)

### No search criteria message
![Search Bar Error](documentation/readme_images/no-search-criteria.png)
</details>

- Users can use the search bar to search for specific products (first image above) that they want to view. The search is matched with the product name and description, as long as the search relates to a product it will show results.
- The user is also shown how many results meet their search (second image above).
- If search criteria does not relate to a product it will not return any results (third image above).
- If a user tries to search without inputting any search criteria an error is shown (fourth image above).

<br>

### Sale Page
<details>
<summary>View sale page</summary>

![Sale image](documentation/readme_images/product-sale.png)
</details>

- This page displays all the sale products, it can also be filtered by gender.

<br>

### Product Details Page
<details>
<summary>View product detail page</summary>

![Product Detail Image](documentation/readme_images/product.detail-page.png)
</details>

- The product detail page displays the product image, name, regular price, sale price (if applicable), brand, category, rating, option to add to wishlist, product description, country of origin, materials, option to select size, select quantity and add product to cart.

<details>
<summary>View Country of origin & Materials Dropdowns</summary>

### Country
![Country](documentation/readme_images/contry-dropdown.png)

### Materials
![Materials](documentation/readme_images/materials-dropdown.png)
</details>

- Country of origin and Materials can be viewed when the dropdown menu is clicked by the user.

<details>
<summary>View review as a signed out user</summary>

![Review not signed in](documentation/readme_images/review-not-signed-in.png)
</details>

- If the user is not signed in they are prompted to do so if they wish to leave a product review.

<details>
<summary>View review as a signed in user</summary>

![Review product](documentation/readme_images/review-product.png)
</details>

- If the user is authorized. they can click on "Review this product" and a dropdown menu will appear.

<details>
<summary>View review drop down</summary>

![Review dropdown](documentation/readme_images/review-dropdown.png)
</details>

- Once clicked, the window opens and the user is able to write a review and hit the submit button.

<details>
<summary>View review success message</summary>

![Review success](documentation/readme_images/review-success.png)
</details>

- When a review is submitted the user will see a success message telling them the review was submitted successfully.

<details>
<summary>View display of a submitted review</summary>

![Review displayed](documentation/readme_images/review-displayed.png)
</details>

<details>
<summary>View edit review page</summary>

![Review edit](documentation/readme_images/edit-review.png)
</details>

- If a users wishes to do so they can edit their review.

<details>
<summary>View edit review success message</summary>

![Review edit success](documentation/readme_images/review-updated.png)
</details>

- When the review is updated a success message is displayed to the user.

<details>
<summary>View delete review page & message</summary>

### Delete review
![Review delete](documentation/readme_images/delete-review.png)

### Delete review message
![Review delete success](documentation/readme_images/delete-review-success.png)
</details>

- If a user decides they want to delete a review they can simply hit the delete review button.
- A success message is displayed once this action is complete.

<details>
<summary>View back to top button</summary>

![Back to Top Button](documentation/readme_images/back-to-top-button.png)
</details>

- To further add to a positive user experience a back to the top button has been added. It is located in the bottom right of the page and once clicked the user will be returned to the top of the given page.

<br>

[Back to Top](#table-of-contents)

### Wishlist Page
<details>
<summary>View wishlist page</summary>

![Wishlist page](documentation/readme_images/wiahlist-with-product-added.png)
</details>

- The wishlist offers the users a place to store all the products that they like and may wish to purchase at a later date.
- The wishlist page provides the product image, name, description, regular or sale price and a link back to the product detail page.
- The page also has a delete button next to each individual product as well as "clear wishlist" button at the top of the page which empties everything from the wishlist if pressed.

<details>
<summary>View empty wishlist</summary>

![Wishlist empty](documentation/readme_images/wishlist-empty.png)
</details>

- If a user is yet to add to their wishlist they will be encouraged to go back and browse the products page.

<details>
<summary>View wishlist icon</summary>

![Wishlist icon](documentation/readme_images/wishlist-icon.png)
</details>

- To add a product to your wishlist, you need to click on the love heart icon.

<details>
<summary>View wishlist success message</summary>

![Wishlist Success](documentation/readme_images/wishlist-success.png)
</details>

- Once a product is successfully added to the wishlist a success message is displayed.

<details>
<summary>View remove from wishlist message</summary>

![Wishlist remove](documentation/readme_images/wishlist-remove-product-message.png)
</details>

- If a user clicks on the heart icon again, this will remove the item from the wishlist and a message will display to confirm this.

<details>
<summary>View view & remove products in the wishlist</summary>

![Wishlist view remove](documentation/readme_images/view-or-remove-product-wishlist.png)
</details>

- When on the wishlist page, if a user clicks on the binoculars icon this redirects you to the products page.
- You can remove an item from the wishlist by clicking the bin icon.

[Back to Top](#table-of-contents)

<br>

### My Account Dropdown Menu

<details>
<summary>View account dropdown as a signed in & signed out user</summary>

### Logged out view
![Logged out](documentation/readme_images/my-account-not-loggedin.png)

### Logged in view
![Logged In](documentation/readme_images/my-account-logged-in.png)
</details>

- If a user is not logged in, they will be given the option to either register for an account or log into an existing account.
- If a user is logged in, the My Account drop-down in the navigation menu will contain a link to the user's profile.
- If the user is logged in and has administrator rights, they will have access to "Product Management".

<details>
<summary>View product management page</summary>

![Product Manage](documentation/readme_images/product-management.png)
</details>

- If the user is logged in and has admin permissions, they can add new products to the site from the admin dropdown in the nav menu by selecting "Product Management".
- The add product page contains a form for the admin to fill out with the details of the new product.

<details>
<summary>View edit existing product page</summary>

![Edit Product](documentation/readme_images/product-management-edit-prod.png)
</details>

- If the user is logged in and has admin permissions, they can edit existing site products by clicking the edit icon on either the product card on the all products page or the individual product details page. 
- The edit product page contains the same form as the add product page but the fields are already populated with the product's current data from the database.

<details>
<summary>View add, edit & delete product messages</summary>

### Add product
![Add](documentation/readme_images/add-prod-msg.png)

### Edit product
![Edit](documentation/readme_images/current-prod-edit.png)

### Delete product
![Delete](documentation/readme_images/product-deleted.png)
</details>

<br>

[Back to Top](#table-of-contents)

<br>

### User sign up page
<details>
<summary>View user sign up</summary>

![Sign up](documentation/readme_images/user-signup.png)
</details>

- Users without an account can register by filling out the sign up form. Once filled out and the sign up button has been pressed the user will then be prompted to verify their email address.

<details>
<summary>View verify email page & email user recieves</summary>

### Verify email page
![Verify](documentation/readme_images/verify-email.png)

### Email to user
![Email](documentation/readme_images/confirm-email.png)
</details>

- When a user has signed up for an account they are instructed to verify their email address.

### User sign in page
<details>
<summary>View sign in page</summary>

![sign in](documentation/readme_images/email-confirmed.png)
</details>

- When a user has verified their email they are then met with a sign in page. They can enter their unique username and password to enter the site as a verified user.
- They can tick the remember me button if they wish.

<details>
<summary>View sign in message</summary>

![sign in msg](documentation/readme_images/success-sigin.png)
</details>

<br>

[Back to Top](#table-of-contents)

<br>

