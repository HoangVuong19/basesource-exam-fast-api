const express = require("express");
const swaggerUi = require("swagger-ui-express");
const SwaggerParser = require("swagger-parser");
const path = require("path");

const app = express();
const swaggerFilePath = path.join(__dirname, "open-api.yaml");

SwaggerParser.bundle(swaggerFilePath)
  .then((swaggerDocument) => {
    // Automatically group APIs by the prefix of the path
    Object.keys(swaggerDocument.paths).forEach((route) => {
      const prefix = route.split('/')[1]; // Get the first part of the URL (vd: "auth")
      Object.values(swaggerDocument.paths[route]).forEach((method) => {
        if (!method.tags) {
          method.tags = [prefix]; // Assign a tag if it doesn't exist
        }
      });
    });

    app.use("/api-docs", swaggerUi.serve, swaggerUi.setup(swaggerDocument));
    app.listen(3001, () => {
      console.log("Swagger UI running at http://localhost:3001/api-docs");
    });
  })
  .catch((error) => {
    console.error("Error loading OpenAPI file:", error);
  });