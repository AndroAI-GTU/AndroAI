import { Module } from '@nestjs/common';
import { UserController } from './user.controller';
import { UserService } from './user.service';
import { FileSystemStoredFile, MemoryStoredFile, NestjsFormDataModule } from 'nestjs-form-data';

@Module({
  imports: [ NestjsFormDataModule.config({
    storage: FileSystemStoredFile,
    fileSystemStoragePath: './tmp/pics',
    cleanupAfterSuccessHandle: false,
  }),],
  controllers: [UserController],
  providers: [UserService]
})
export class UserModule {}
