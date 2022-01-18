# Inquizitive
Navigate to folder containing code: <br />
Run: "cd inquizitive"

## Getting Started:
1. Follow "Clean Docker Instance" steps
2. Follow "Production Server" steps
3. Follow "Interacting with Application" steps

## Clean Docker Instance
Run: "docker system prune" <br />
Run: "docker volume prune" <br />
Run: "docker network prune" <br />

## Production Server:
Run: "docker-compose -f docker-compose.prod.yml up --build" <br />
Visit: "localhost:8080" <br />
Run: "docker-compose down" <br />

## Development Server (Optional):
Run: "docker-compose up --build" <br />
Visit: "localhost:8080" <br />
Run: "docker-compose down" <br /> 


## Interacting with Application
To explore all the features of our website, we suggest you follow these simple steps:
1. Register for an account & Login
2. Try out a sample quiz in the Technology genre
3. Create your own quiz
4. Change your profile picture or profile details via the profile page.
5. View your quizzes and edit them via your profile.
6. View statistics about your previous quiz attempts on your profile.