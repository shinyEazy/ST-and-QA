import java.util.regex.*;

public class RegistrationValidator {
    public static String validateRegistration(String email, String password, String confirmPassword) {
        String noti = "Success";
        
        String emailPattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z]+\\.com$";
        if (Pattern.matches(emailPattern, email)) {
            if (password.length() >= 8 && password.length() <= 24) {
                if (password.chars().anyMatch(Character::isUpperCase)) {
                    if (password.chars().anyMatch(Character::isDigit)) {
                        if (password.equals(confirmPassword)) {
                            noti = "Success";
                        } else {
                            noti = "Password mismatch";
                        }
                    } else {
                        noti = "Invalid password";
                    }
                } else {
                    noti = "Invalid password";
                }
            } else {
                noti = "Invalid password";
            }
        } else {
            noti = "Invalid email";
        }
        
        return noti;
    }
}