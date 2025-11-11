import java.io.File;
import java.util.Arrays;

public class BackupUpdater {
    public static void main(String args[]) {
        String folder_path = "myFolder";
        String backup_path = "myFolder-backup";

        File folder = new File(folder_path);
        File backup = new File(backup_path);

        boolean folder_valid, backup_valid;

        folder_valid = checkValidity(folder, "folder");
        backup_valid = checkValidity(backup, "backup");

        if(folder_valid && backup_valid) {
            compareFolders(folder, backup, folder_path, backup_path);
        }
    } // end of main

    static boolean checkValidity(File f, String name_type) {
        if((!f.exists())) {
            System.out.println("The " + name_type + " path you have provided does not exist.");
            return false;
        } else {
            if(f.isFile()) {
                System.out.println("The " + name_type + " path you have provided is not a directory.");
                return false;
            } else {
                System.out.println("Valid!");
                return true;
            }
        } // end of else
    }

    static void compareFolders(File dir_1, File dir_2, String path_1, String path_2) {
        // list folder content
        String[] list_1 = dir_1.list();
        String[] list_2 = dir_2.list();

        

        /* int file_count_1 = 0;
        int file_count_2 = 0;

        for(int i=0; i<list_1.length; i++) {
            file_count_1++;
        }
        for(int i=0; i<list_2.length; i++) {
            file_count_2++;
        } 

        System.out.println(file_count_1);
        System.out.println(file_count_2); */

        if(Arrays.equals(list_1, list_2)) {
            // compare properties of all files
            for(int i=0; i<list_1.length; i++) {
                File f1 = new File(path_1 + "/" + list_1[i]);
                File f2 = new File(path_2 + "/" + list_2[i]);

                if(f1.lastModified() == f2.lastModified()) {
                    continue;
                } else {

                }
            }
        } else {
            System.out.println("updating backup folder...");
        }

        // compare properties of files that are the same
        // if different properties, take file from dir_1 and replace said file in dir_2

        // if dir_1 has file that dir_2 doesnt have, copy said file from dir_1 to dir_2
    }
}
// placeholder file