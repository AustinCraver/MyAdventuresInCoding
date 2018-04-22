/*
 * This amazing Java game was written by Austin Craver
 * by following and coding along with a 57 minute tutorial.
 * Special thanks to Awais Mirza for taking the time to create
 * and share such a helpful and informative video!!! * 
 */

package breakerGame;

import javax.swing.JFrame;

public class Main {

    public static void main(String[] args) {
        // Creates frame for game
        JFrame obj = new JFrame();
        Gameplay gamePlay = new Gameplay();
        obj.setBounds(10, 10, 700, 600);
        obj.setTitle("Breakout Ball");
        obj.setResizable(false);
        obj.setVisible(true);
        obj.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        obj.add(gamePlay);
    }
}
