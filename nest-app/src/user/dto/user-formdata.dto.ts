import { Expose } from 'class-transformer';
import { FileSystemStoredFile, HasMimeType, IsFile, MaxFileSize } from 'nestjs-form-data';

export class Activity{
    @Expose()
    name: string;
    
    @Expose()
    content: string;

    @Expose()
    links: string[];
}

export class UserFormDataDto {
    @Expose()
    appName: string;

    @Expose()
    activities: Activity[];
    
    @Expose()
    generalExplaining: string;

    @Expose()
    @IsFile()
    @MaxFileSize(1e6)
    @HasMimeType(['image/jpeg', 'image/png'])
    appIcon: FileSystemStoredFile;

}
