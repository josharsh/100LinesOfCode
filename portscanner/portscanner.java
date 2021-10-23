import java.awt.*;
import java.io.IOException;
import java.net.*
import javax.swing.*;

public class PortScanner extends JFrame implements ActionListener, ChangeListener {
	
	private static final long serialVersionUID = 2884600754343147821L; //Final variables
	private static final int W = 250;
	private static final int H = 375;	
	private boolean displayAll = false; //Flags
	private JTextField ipAddress, lowerPort, higherPort; //Compoents
	private JTextArea output;
	private JScrollPane outputScroller;
	private JCheckBox toggleDisplayAll;
	private JButton scanPorts;
	private JPanel settingsPanel, outputPanel;
	
	public PortScanner() { // Sets up the frame and calls
		super( "Port Scanner" );
		initComponents();
		super.setLayout( new FlowLayout() );
		super.setSize( W, H );
		super.setLocationRelativeTo( null );
		super.setResizable( false );
		super.setVisible( true );
		super.setDefaultCloseOperation( JFrame.EXIT_ON_CLOSE );
	}
	private void initComponents() {  //  Sets up the components, panels, and adds them to the Frame
		
		this.ipAddress = new JTextField( 12 ); //Text fields
		this.lowerPort = new JTextField( 5 );
		this.higherPort = new JTextField( 5 );
		this.output = new JTextArea( 10, 20 ); //TextArea & ScrollPane
		this.output.setEditable( false );
		this.output.setLineWrap( true );
		this.outputScroller = new JScrollPane( this.output );
		this.toggleDisplayAll = new JCheckBox( "Display all results (open & closed)" ); //Check box
		this.toggleDisplayAll.addChangeListener( this );
		this.scanPorts = new JButton( "Scan" ); //Buttons
		this.scanPorts.addActionListener( this );
		this.settingsPanel = new JPanel( new FlowLayout() ); //JPanels
		this.settingsPanel.setBorder( BorderFactory.createTitledBorder( "Scan information" ) );
		this.settingsPanel.setPreferredSize( new Dimension( 230, 135 ) );
		this.settingsPanel.add( new JLabel( "IP Address: " ) );
		this.settingsPanel.add( this.ipAddress );
		this.settingsPanel.add( new JLabel( "Port range: " ) );
		this.settingsPanel.add( this.lowerPort );
		this.settingsPanel.add( new JLabel( "-" ) );
		this.settingsPanel.add( this.higherPort );
		this.settingsPanel.add( this.toggleDisplayAll );
		this.settingsPanel.add( this.scanPorts );
		this.outputPanel = new JPanel( new FlowLayout() );
		this.outputPanel.setBorder( BorderFactory.createTitledBorder( "Results: " ) );
		this.outputPanel.add( outputScroller );	
		super.add( this.settingsPanel );
		super.add( this.outputPanel ); //add components
	}
        @Override
	public void actionPerformed(ActionEvent ae ) { // manages button action
		if( ae.getSource() == this.scanPorts ) {
			this.output.setText("Starting scan..." + System.lineSeparator() );
			scan( this.ipAddress.getText(), this.lowerPort.getText(), this.higherPort.getText(), 200 );
			this.output.append( "Scan finished." );
		}}
        @Override
	public void stateChanged(ChangeEvent ce) {
		if( ce.getSource() == toggleDisplayAll ) {
			this.displayAll = this.toggleDisplayAll.isSelected();
		}}
	private void scan( String ipAddress, String lowPort, String highPort, int timeout ) {
		int start, end;  //Scans the specified ip address and tests the ports in the given range

		try {		//verify port numbers
			start = Integer.parseInt( lowPort );
			end = Integer.parseInt( highPort );
			
			if( end <= start ) {
				this.output.append( "The second port must be higher than the first port" + System.lineSeparator() );
				return;
			}}
		catch( NumberFormatException nfe ) {
			this.output.append( "Please enter valid port numbers." + System.lineSeparator() );
			return;
		}
		for( int current = start; current <= end; current++ ) { //Scan ports in range
			try {
                            try (Socket s = new Socket()) {
                                s.connect( new InetSocketAddress( ipAddress, current ), timeout ); //attempt a connection
                            } //attempt a connection
				
				this.output.append( "Open port: " + current + System.lineSeparator() );
			}
			catch( IOException ioe ) { //connection failed
				if( this.displayAll ) {
					this.output.append( "Closed port: " + current + System.lineSeparator() );
				}}}}
	public static void main( String[] args ) {
		@SuppressWarnings("unused")
		PortScanner psg = new PortScanner(); // creates instance of GUI
	}}