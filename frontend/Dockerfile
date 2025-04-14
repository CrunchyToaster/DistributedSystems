# Use an official Node.js runtime
FROM node:slim

# Create app directory
WORKDIR /app

# Copy package.json and package-lock.json / yarn.lock
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy all Nuxt code
COPY . .

# Expose port 3000 for Nuxt dev server
EXPOSE 3000

# Run the dev server
CMD ["npm", "run", "dev"]
