package view;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JButton;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.SwingConstants;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.Font;

public class BinToDec {

	private JFrame frame;
	private JTextField tfBin;

	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					BinToDec window = new BinToDec();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}
	
	public BinToDec() {
		initialize();
	}
	
	private void initialize() {
		frame = new JFrame();
		frame.setBounds(100, 100, 450, 300);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);
		
		JLabel lblDec = new JLabel("Result Here");
		lblDec.setFont(new Font("Tahoma", Font.PLAIN, 26));
		lblDec.setHorizontalAlignment(SwingConstants.CENTER);
		lblDec.setBounds(33, 36, 364, 127);
		frame.getContentPane().add(lblDec);
		
		JButton btnConvert = new JButton("Convert");
		btnConvert.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				int dec = 0;
				for(int i = 1; i <= tfBin.getText().length(); i++) {
					dec += (Character.getNumericValue(tfBin.getText().charAt(i - 1)) * Math.pow(2, tfBin.getText().length() - i));
				}
				lblDec.setText("" + dec);
			}
		});
		btnConvert.setBounds(168, 205, 89, 23);
		frame.getContentPane().add(btnConvert);
		
		tfBin = new JTextField();
		tfBin.setBounds(54, 174, 315, 20);
		frame.getContentPane().add(tfBin);
		tfBin.setColumns(10);
	}
}