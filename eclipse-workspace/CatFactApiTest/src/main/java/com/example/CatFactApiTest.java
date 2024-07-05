package com.example;

import io.restassured.RestAssured;
import io.restassured.response.Response;
import org.testng.Assert;
import org.testng.annotations.Test;

public class CatFactApiTest {

    @Test
    public void testGetCatFact() {
        // Make the API call
        Response response = RestAssured.get("https://catfact.ninja/fact");

        // Validate the response status code
        Assert.assertEquals(response.getStatusCode(), 200);

        // Print the response body
        String responseBody = response.getBody().asString();
        System.out.println("Response Body: " + responseBody);

        // Validate the response content
        String fact = response.jsonPath().getString("fact");
        Assert.assertNotNull(fact, "Fact should not be null");
        System.out.println("Cat Fact: " + fact);
    }
}
