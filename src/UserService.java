package src;

import java.util.List;
import java.util.ArrayList;

/**
 * Service class for managing user operations.
 * Provides functionality to create, retrieve, and manage users in the system.
 * 
 * @author Documentation Generator Test
 * @version 1.0
 * @since 2024
 */
public class UserService {
    
    /** List to store all users in memory */
    private List<User> users;
    
    /**
     * Constructs a new UserService with an empty user list.
     */
    public UserService() {
        this.users = new ArrayList<>();
    }
    
    /**
     * Creates a new user and adds it to the system.
     * 
     * @param name The user's full name
     * @param email The user's email address
     * @return The created User object
     * @throws IllegalArgumentException if name or email is null or empty
     */
    public User createUser(String name, String email) {
        if (name == null || name.trim().isEmpty()) {
            throw new IllegalArgumentException("Name cannot be null or empty");
        }
        if (email == null || email.trim().isEmpty()) {
            throw new IllegalArgumentException("Email cannot be null or empty");
        }
        
        User user = new User(name, email);
        users.add(user);
        return user;
    }
    
    /**
     * Retrieves a user by their email address.
     * 
     * @param email The email address to search for
     * @return The User object if found, null otherwise
     */
    public User getUserByEmail(String email) {
        return users.stream()
                   .filter(user -> user.getEmail().equals(email))
                   .findFirst()
                   .orElse(null);
    }
    
    /**
     * Gets the total number of users in the system.
     * 
     * @return The count of users
     */
    public int getUserCount() {
        return users.size();
    }
    
    /**
     * Simple User class representing a system user.
     */
    public static class User {
        private String name;
        private String email;
        
        /**
         * Constructs a new User.
         * 
         * @param name The user's name
         * @param email The user's email
         */
        public User(String name, String email) {
            this.name = name;
            this.email = email;
        }
        
        /** @return The user's name */
        public String getName() { return name; }
        
        /** @return The user's email */
        public String getEmail() { return email; }
    }
}