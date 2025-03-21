import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class RegistrationValidatorTest {
    
    @Test
    void testValidateRegistration() {
        assertEquals("Invalid password", RegistrationValidator.validateRegistration("shiny@gmail.com", "123", "12345678")); 
        assertEquals("Invalid email", RegistrationValidator.validateRegistration("shiny@gmail.co", "12345678", "12345678"));
        assertEquals("Invalid password", RegistrationValidator.validateRegistration("shiny@gmail.com", "123456anh", "123456anh")); 
        assertEquals("Invalid password", RegistrationValidator.validateRegistration("shiny@gmail.com", "123", "12345678")); 
        assertEquals("Invalid password", RegistrationValidator.validateRegistration("shiny@gmail.com", "anhanhanh", "anhanhanh")); 
        assertEquals("Invalid password", RegistrationValidator.validateRegistration("shiny@gmail.com", "123456anh", "123456anh")); 
        assertEquals("Password mismatch", RegistrationValidator.validateRegistration("shiny@gmail.com", "123456Anh", "123456An")); 
        assertEquals("Invalid password", RegistrationValidator.validateRegistration("shiny@gmail.com", "anhanhanh", "anhanhanh")); 
        assertEquals("Success", RegistrationValidator.validateRegistration("shiny@gmail.com", "123456Anh", "123456Anh")); 
        assertEquals("Password mismatch", RegistrationValidator.validateRegistration("shiny@gmail.com", "123456Anh", "123456An")); 
        assertEquals("Success", RegistrationValidator.validateRegistration("shiny@gmail.com", "123456Anh", "123456Anh"));
        assertEquals("Password mismatch", RegistrationValidator.validateRegistration("shiny@gmail.com", "123456Anh", "123456An")); 
        assertEquals("Invalid email", RegistrationValidator.validateRegistration("shiny@gmail.co", "12345678", "12345678"));
        assertEquals("Invalid email", RegistrationValidator.validateRegistration("shiny@gmail.co", "12345678", "12345678"));
        assertEquals("Invalid password", RegistrationValidator.validateRegistration("shiny@gmail.com", "123", "12345678")); 
        assertEquals("Invalid password", RegistrationValidator.validateRegistration("shiny@gmail.com", "123456anh", "123456anh")); 
        assertEquals("Invalid password", RegistrationValidator.validateRegistration("shiny@gmail.com", "anhanhanh", "anhanhanh"));
        assertEquals("Invalid password", RegistrationValidator.validateRegistration("shiny@gmail.com", "123", "12345678"));
        assertEquals("Invalid email", RegistrationValidator.validateRegistration("shiny@gmail.co", "12345678", "12345678")); 
    }
}
