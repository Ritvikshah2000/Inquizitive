# Production Deployment of Inquizitive

## Change Directory
Run: "cd inquizitive"

## Development Server:
Run: "docker-compose up --build" <br />
Visit: "localhost:8080" <br />
Run: "docker-compose down" <br /> 

## Production Server:
Run: "docker-compose -f docker-compose.prod.yml up --build" <br />
Visit: "localhost:8080" <br />
Run: "docker-compose down" <br />

## Clean Docker Instance
Run: "docker system prune" <br />
Run: "docker volume prune" <br />
Run: "docker network prune" <br />