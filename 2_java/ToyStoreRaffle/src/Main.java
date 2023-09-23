import java.util.ArrayList;
import java.util.List;
import java.util.Random;

class Main {
    private List<Toy> toys;

    public Main() {
        toys = new ArrayList<>();
    }

    // Метод для добавления новой игрушки
    public void addToy(Toy toy) {
        toys.add(toy);
    }

    // Метод для проведения розыгрыша
    public Toy drawToy() {
        if (toys.isEmpty()) {
            System.out.println("В магазине нет игрушек.");
            return null;
        }

        Random random = new Random();
        int totalWeight = 0;

        for (Toy toy : toys) {
            totalWeight += toy.getWeight();
        }

        int randomNumber = random.nextInt(totalWeight);
        int currentIndex = 0;

        for (Toy toy : toys) {
            currentIndex += toy.getWeight();

            if (randomNumber < currentIndex) {
                System.out.println("Выпала игрушка: " + toy.getName());
                return toy;
            }
        }

        return null;
    }

    public static void main(String[] args) {
        Main toyStore = new Main();

        // Пример добавления игрушек
        toyStore.addToy(new Toy("Мяч", 5));
        toyStore.addToy(new Toy("Кукла", 7));
        toyStore.addToy(new Toy("Машинка", 3));

        // Пример проведения розыгрыша
        Toy winner = toyStore.drawToy();

        if (winner != null) {
            System.out.println("Поздравляем победителя! Игрушка: " + winner.getName());
        }
    }
}