
<a name="readme-top"></a>




<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/barillamw/WebApp-Portfolio">
    <img src="./image.png" alt="Logo" height="80">
  </a>

<h3 align="center">Workout Tracking API</h3>

  <p align="center">
    <!-- <br />
    <a href="https://github.com/barillamw/WebApp-Portfolio"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/barillamw/WebApp-Portfolio">View Demo</a>
    ·
    <a href="https://github.com/barillamw/WebApp-Portfolio/issues">Report Bug</a>
    ·
    <a href="https://github.com/barillamw/WebApp-Portfolio/issues">Request Feature</a> -->
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com)` -->

<p> A comprehensive solution for logging and managing workout routines and exercises. Built on Django, this RESTful API provides a robust backend to support your fitness journey. With a MySQL Server database and future plans for a Flutter UI, this API is designed to seamlessly track and visualize your workout progress.</p>

### Exercise Logging and Tracking
The Workout Tracker API enables users to log their exercises and workouts efficiently. With a range of predefined exercises and the flexibility to create custom exercises, users can tailor their fitness routines to match their goals.

### Routine Management
Users can organize exercises into workout routines. The API allows users to create, modify, and delete routines based on their preferences. This feature ensures that users can easily switch between different workout plans.

### MySQL Database
The API is powered by a MySQL database, which ensures secure and efficient storage of exercise and routine data. This relational database structure allows for smooth data retrieval and manipulation.

### Future - Flutter UI
In the future, a Flutter-based user interface will be integrated with the API. This UI will provide users with a mobile platform to access their workout data, view progress charts, and receive workout recommendations based on their history.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With
[![Django][Django]][Django-url]
[![Python][Python]][Python-url]
[![MySQL][MySQL]][MySQL-url]
[![Flutter][Flutter]][Flutter-url]
[![Azure][Azure]][Azure-url]

* **Django**: The core framework used to build the RESTful API, providing a structured and efficient way to manage workout data.

* **MySQL Database**: The chosen relational database backend for storing exercise and routine data securely.

* **Azure App Service**: The API is hosted on Azure's App Service, ensuring reliable and scalable hosting solutions.

* **Flutter (Future)**: The planned mobile UI to give users easy access to their workout data and progress charts.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

1. **Clone the Repository**: Clone the repository containing the Django project.

2. **Set Up SQL Server**: Configure the SQL Server database connection settings in the Django project's settings file.

3. **Run Migrations**: Run database migrations to set up the initial schema: python manage.py makemigrations followed by python manage.py migrate.

4. **Start the Development Server**: Launch the Django development server to test and interact with the API.

5. **Access API Endpoints**: Use tools like curl, Postman, or any HTTP client to interact with the API's endpoints for exercise and routine management.

6. **(Future) Flutter UI**: Stay tuned for the upcoming Flutter UI that will provide users with mobile access to their workout data.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Build Workout, Exercise and Set Endpoints
- [ ] Create a user Interface
- [ ] Build in User Token based Authentication
- [ ] Build library of workouts
- [ ] Increase user interaction with additional features

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LESSONS -->
## Lessons Learned
Previously I had worked with pre-built APIs, but building one I found it interesting to see all of the different views that had to be thought through. This helped me get a better grasp on how to structure databases to reference the necessary information. User authentication to the API was a challenge learning how to implement and ensure security of data. 

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Michael Barilla - mbarill@ncsu.edu.com

Begin your fitness journey with the Workout Tracker API, built on Django and hosted on Azure. Log your exercises, manage routines, and harness the power of data to achieve your fitness goals. With a planned Flutter UI on the horizon, accessing and visualizing your workout progress will be more convenient than ever before.

Project Link: [https://github.com/barillamw/WebApp-Portfolio](https://github.com/barillamw/WebApp-Portfolio)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/barillamw/WebApp-Portfolio.svg?style=for-the-badge
[contributors-url]: https://github.com/barillamw/WebApp-Portfolio/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/barillamw/WebApp-Portfolio.svg?style=for-the-badge
[forks-url]: https://github.com/barillamw/WebApp-Portfolio/network/members
[stars-shield]: https://img.shields.io/github/stars/barillamw/WebApp-Portfolio.svg?style=for-the-badge
[stars-url]: https://github.com/barillamw/WebApp-Portfolio/stargazers
[issues-shield]: https://img.shields.io/github/issues/barillamw/WebApp-Portfolio.svg?style=for-the-badge
[issues-url]: https://github.com/barillamw/WebApp-Portfolio/issues
[license-shield]: https://img.shields.io/github/license/barillamw/WebApp-Portfolio.svg?style=for-the-badge
[license-url]: https://github.com/barillamw/WebApp-Portfolio/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/michael-barilla
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[C]: https://img.shields.io/badge/c-%2300599C.svg?style=for-the-badge&logo=c&logoColor=white
[C-url]: https://www.open-std.org/jtc1/sc22/wg14/
[Arduino]: https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white
[Arduino-url]: https://www.arduino.cc/
[RapsberryPi]: https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&logo=Raspberry-Pi
[RaspberryPi-url]: https://www.raspberrypi.com/
[CPP]: https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white
[CPP-url]: https://isocpp.org/
[Gatsby]:https://img.shields.io/badge/Gatsby-%23663399.svg?style=for-the-badge&logo=gatsby&logoColor=white
[Gatsby-url]: https://www.gatsbyjs.com/
[Azure]: https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white
[Azure-url]: https://azure.microsoft.com/en-us/
[HTML5]: https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white
[HTML5-url]:https://html.spec.whatwg.org/multipage/
[Bootstrap]: https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com/
[Markdown]: https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white
[Markdown-url]: https://daringfireball.net/projects/markdown/
[Django]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white
[Django-Url]: https://www.djangoproject.com/
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[MySQL]: https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white
[MySQL-url]: https://www.mysql.com/
[Flutter]: https://img.shields.io/badge/Flutter-%2302569B.svg?style=for-the-badge&logo=Flutter&logoColor=white
[Flutter-url]: https://flutter.dev/