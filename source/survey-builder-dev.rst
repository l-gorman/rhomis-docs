.. _survey_builder_dev:

Survey Builder 
==================================

Essential information
-----------------------------------

The code for the RHoMIS 2.0 survey builder can be found `here <https://github.com/stats4sd/survey-builder>`_.
The application is written using laravel.

The survey builder requests infromation from:

* The authentication server

The survey builder gives information to the following components of RHoMIS 2.0:

* RHoMIS ODK central server
* RHoMIS database
* Analysis Scripts

Processes
------------------------------------

.. image:: images/survey_builder_process.png

Note how the survey builder works throughout the process. It saves information in its own database and also
synchronises with other applications in RHoMIS 2.0. When a user registers, their credentials 
are saved in a centralised RHoMIS 2.0 authentication server. The user id is then saved in the survey builder
database, along with the email. Projects, forms, and metadata are stored in the survey builder db as well as 
in ODK central.

Database 
------------------------------------

Projects
************************************

Users
************************************

Survey Form 
************************************


Survey Module 
************************************

.. image:: images/survey_modules.png


