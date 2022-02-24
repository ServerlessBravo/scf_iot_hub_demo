package example;

import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Date; 
import java.text.SimpleDateFormat; 


public class Hello {
    public String mainHandler(String inputData) {
        System.out.println("Input test string:"+ inputData);
        final String regex = "TimeMills.*?(\\d+),";
        final Pattern pattern = Pattern.compile(regex, Pattern.MULTILINE);
        final Matcher matcher = pattern.matcher(inputData);
        
        while (matcher.find()) {
            System.out.println("Full match: " + matcher.group(0));
            
            for (int i = 1; i <= matcher.groupCount(); i++) {
                final String senderEpochInString = matcher.group(i);
                System.out.println("Group " + i + ": " + senderEpochInString);

                long timeMills = Long.parseLong(senderEpochInString);
                Date senderDate = new Date(timeMills);

                SimpleDateFormat jdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
                String java_date = jdf.format(senderDate);

                System.out.println("Sender time: " + java_date );
                
                SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");  
                Date currentDate = new Date();  
                System.out.println("Current time: " + formatter.format(currentDate));  

                long differenceInTime = currentDate.getTime() - senderDate.getTime();
                System.out.println("Time difference is : " + differenceInTime + " ms");  
            
            }
        }

        return "success";
    }
}