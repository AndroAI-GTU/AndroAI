import { Expose } from 'class-transformer';
import { FileSystemStoredFile, HasMimeType, IsFile, MaxFileSize } from 'nestjs-form-data';

export class UserFormDataDto {
    @Expose()
    appName: string;

    @Expose()
    activityCount: number;

    @Expose()
    activityNames: string;

    @Expose()
    activityConnections: string;

    @Expose()
    activityElements: string;

    @Expose()
    elementFunctions: string;

    @Expose()
    @IsFile()
    @MaxFileSize(1e6)
    @HasMimeType(['image/jpeg', 'image/png'])
    appIcon: FileSystemStoredFile;


}