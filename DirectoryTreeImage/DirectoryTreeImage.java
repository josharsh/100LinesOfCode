import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.util.*;
import java.util.List;
import javax.imageio.ImageIO;

public class DirectoryTreeImage {
    static List<String> entries = new ArrayList<>(); // Format: Prefix::Name::Size
    // Ignore list to keep tree clean (you can modify as needed)
    static final Set<String> IGNORED = new HashSet<>(Arrays.asList(".git", "node_modules", "target", ".idea", "bin", "obj", "build"));
    static int fileCount = 0, dirCount = 0;
    public static void main(String[] args) throws Exception {
        Scanner s = new Scanner(System.in);
        System.out.print("Path (Enter for current): ");
        String in = s.nextLine().trim();
        File root = new File(in.isEmpty() ? "." : in).getCanonicalFile();
        if (!root.exists()) {
            System.out.println("Path not found:" + root.getAbsolutePath());
            return;
        }
        // Add root manually (ensure 3 parts: prefix is empty, name, size is empty)
        entries.add("::" + root.getName() + "::"); 
        walk(root, "");
        // Print to console
        entries.forEach(e -> System.out.println(e.replace("::", " "))); 
        try {
            Font font = new Font("Consolas", Font.PLAIN, 14);
            BufferedImage tmp = new BufferedImage(1, 1, 1);
            FontMetrics fm = tmp.createGraphics().getFontMetrics(font);            
            // Calculate max width
            int maxW = entries.stream().mapToInt(e -> fm.stringWidth(e.replace("::", " "))).max().orElse(400);
            int rowH = fm.getHeight() + 6;
            int h = entries.size() * rowH + 60; // Extra space for footer
            int w = maxW + 100;

            BufferedImage img = new BufferedImage(w, h, BufferedImage.TYPE_INT_RGB);
            Graphics2D g = img.createGraphics();
            g.setRenderingHint(RenderingHints.KEY_TEXT_ANTIALIASING, RenderingHints.VALUE_TEXT_ANTIALIAS_ON);
            g.setFont(font);
            // Draw Rows
            for (int i = 0; i < entries.size(); i++) {
                g.setColor(i % 2 == 0 ? new Color(40, 44, 52) : new Color(44, 49, 58)); // Zebra striping
                g.fillRect(0, i * rowH, w, rowH);
                //Added limit -1 to keep empty strings (prevent IndexOutOfBounds)
                String[] parts = entries.get(i).split("::", -1);
                
                int y = (i * rowH) + fm.getAscent() + 3;
                int x = 20;
                // 1. Structure (Prefix)
                g.setColor(new Color(100, 100, 100)); 
                if (parts.length > 0) {
                    g.drawString(parts[0], x, y);
                    x += fm.stringWidth(parts[0]);
                }
                // 2. Icon & Name
                String name = parts.length > 1 ? parts[1] : "";
                String size = parts.length > 2 ? parts[2] : "";
                boolean isFile = size.trim().length() > 0;
                g.setColor(isFile ? new Color(224, 108, 117) : new Color(229, 192, 123)); // Red vs Gold
                if (isFile) g.fillOval(x + 2, y - 8, 6, 6); else g.fillRect(x + 2, y - 8, 8, 7);
                g.setColor(isFile ? new Color(171, 178, 191) : new Color(97, 175, 239)); // Gray vs Blue
                g.drawString(name, x + 18, y);
                // 3. File Size (Dimmed)
                if (isFile) {
                    g.setColor(new Color(92, 99, 112));
                    g.drawString("(" + size + ")", x + 18 + fm.stringWidth(name) + 10, y);
                }
            }
            // Footer
            g.setColor(new Color(33, 37, 43)); g.fillRect(0, h - 35, w, 35);
            g.setColor(Color.WHITE); 
            g.drawString(String.format("SUMMARY: %d Folders, %d Files scanned", dirCount, fileCount), 20, h - 12);            
            g.dispose();
            ImageIO.write(img, "png", new File("tree_structure.png"));
            System.out.println("[+] Saved report to tree_structure.png");
        } catch (Exception e) { 
            e.printStackTrace(); 
        }
    }
    private static void walk(File folder, String prefix) {
        File[] files = folder.listFiles();
        if (files == null) return;
        
        Arrays.sort(files, (a, b) -> {
            if (a.isDirectory() == b.isDirectory()) return a.getName().compareToIgnoreCase(b.getName());
            return a.isDirectory() ? -1 : 1;
        });
        for (int i = 0; i < files.length; i++) {
            File f = files[i];
            if (IGNORED.contains(f.getName())) continue;
            
            boolean last = (i == files.length - 1);
            String size = "";
            if (f.isDirectory()) { 
                dirCount++; 
            } else { 
                fileCount++; 
                long b = f.length();
                size = (b < 1024) ? b + " B" : (b / 1024) + " KB";
            }
            // Format: Prefix::Name::Size (Size is empty for folders)
            entries.add(prefix + (last ? "└──" : "├──") + "::" + f.getName() + "::" + size);           
            if (f.isDirectory()) walk(f, prefix + (last ? "    " : "│   "));
        }
    }
}
