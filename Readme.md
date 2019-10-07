# Gallery

This python/django web-app was created in order to display my images in a gallery format.

By: Robin kariuki

## Description
This web-app allows the user to view teh admin's images while allowing the admin to add the images according with the following attributes: Location and Category.

## Setup/Installation Requirements

*   Fork the repository
*   git clone the project to your local machine
*   Set up a virtual environment in the project folder
```
python3.6 -m venv --without-pip virtual
```

### Prerequisites

*get pip 

```
curl https://bootstrap.pypa.io/get-pip|python
```

*get all requirements in the requirements.txt file

```
pip install -r requirements.txt
```

### Installing

Ensure that the MODE in the .env is set to development ('dev'), which will automatically set debug to true.

Now run the following command

```
python3.6 manage.py runserver
```

And view the site at the port provided which is most likely 127.0.0.1:8000

### Known Bugs
images are not properly arranged.

### Behaviour Driven Development
* The program should return all images on the home page<br>
Given:All images<br>
When: Url is changed to home page<br>
Then: All Images are displayed<br>

* Modal should be displayed when the user clicks on any image and have the image's details<br>
Given:An image<br>
When: User cicks on the image <br>
Then: A modal with the image's details is displayed<br>

* Admin site should be displayed when "admin/" url is chosen<br>
Given: An admin url<br>
When: User enters admin url in browser<br>
Then: Admin Login is displayed<br>

* User authentication occurs when Admin tries to Login<br>
Given:Admin page is accessed<br>
When: User tries to login<br>
Then: User details are authenticated to confirm if user is an admin<br>


### Technologies Used
* Python3.6
* Django Web Framework
* Bootstrap4 

### Support and contact details
* Contact me through my email: robinkariuki123@gmail.com
* The source code is also contained within the folder containing this ReadMe with comments on the code thus third-party support can be offered.

## Licence
 
 [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](http://opensource.org/licenses/MIT)
 
 
 Copyright (c) 2019 RobinKariuki
