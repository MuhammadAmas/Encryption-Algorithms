public class VernamCipher {

    public static String vernamEncrypt(String plaintext, String key) {
        // Ensure the key is at least as long as the plaintext
        if (key.length() < plaintext.length()) {
            System.out.println("Key length must be at least as long as plaintext");
            return "";
        }

        // Convert plaintext and key to uppercase
        plaintext = plaintext.toUpperCase();
        key = key.toUpperCase();

        // Perform XOR operation for each character
        StringBuilder encryptedText = new StringBuilder();
        for (int i = 0; i < plaintext.length(); i++) {
            char encryptedChar = (char) (((plaintext.charAt(i) - 65) + (key.charAt(i) - 65)) % 26 + 65);
            encryptedText.append(encryptedChar);
        }

        return encryptedText.toString();
    }

    public static String vernamDecrypt(String encryptedText, String key) {
        // Ensure the key is at least as long as the encrypted text
        if (key.length() < encryptedText.length()) {
            System.out.println("Key length must be at least as long as encrypted text");
            return "";
        }

        // Convert key to uppercase
        key = key.toUpperCase();

        // Perform XOR operation for each character
        StringBuilder decryptedText = new StringBuilder();
        for (int i = 0; i < encryptedText.length(); i++) {
            char decryptedChar = (char) (((encryptedText.charAt(i) - key.charAt(i)) % 26 + 26) % 26 + 65);
            decryptedText.append(decryptedChar);
        }

        return decryptedText.toString();
    }

    public static void main(String[] args) {
        String plaintext = "CIPHER";
        String key = "ENCODE";

        System.out.print("Plaintext: " + plaintext + "\n");
        System.out.print("Key: " + key + "\n");

        // Encrypt the message
        String encryptedText = vernamEncrypt(plaintext, key);
        System.out.println("Encrypted Text: " + encryptedText);

        // Decrypt the message
        String decryptedText = vernamDecrypt(encryptedText, key);
        System.out.println("Decrypted Text: " + decryptedText);
    }
}
