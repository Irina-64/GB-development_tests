import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class ToyStore {
    private static final String[] TOY_IDS = {"1", "2", "3"};
    private static final String[] TOY_NAMES = {"конструктор", "робот", "кукла"};
    private static final int[] TOY_WEIGHTS = {20, 20, 60}; // Веса в процентах

    private FileWriter fileWriter;

    public ToyStore() {
        try {
            fileWriter = new FileWriter("output.txt");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public String getToy() {
        Random random = new Random();
        int randomNumber = random.nextInt(100);

        int cumulativeWeight = 0;
        for (int i = 0; i < TOY_WEIGHTS.length; i++) {
            cumulativeWeight += TOY_WEIGHTS[i];
            if (randomNumber < cumulativeWeight) {
                return TOY_IDS[i];
            }
        }

        return null;
    }

    public void writeToFile(String value) {
        try {
            fileWriter.write(value + "\n");
            fileWriter.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void closeFile() {
        try {
            fileWriter.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        ToyStore toyStore = new ToyStore();
        Random random = new Random();

        for (int i = 0; i < 10; i++) {
            String toy = toyStore.getToy();
            toyStore.writeToFile(toy);
        }

        toyStore.closeFile();
    }
}
